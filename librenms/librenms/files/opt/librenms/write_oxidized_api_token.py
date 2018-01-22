#! /usr/bin/env python2
try:

    import json
    import os
    import subprocess
    import sys
    import binascii
    import argparse

except:
    print("ERROR: missing one or more of the following python modules:")
    print("threading, Queue, sys, subprocess, time, os, json")
    sys.exit(2)

try:
    import MySQLdb
except:
    print("ERROR: missing the mysql python module:")
    print("On ubuntu: apt-get install python-mysqldb")
    print("On FreeBSD: cd /usr/ports/*/py-MySQLdb && make install clean")
    sys.exit(2)


# Fetch configuration details from the config_to_json.php script
def get_config_data():
    install_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = install_dir + '/config.php'

    try:
        with open(config_file) as f:
            pass
    except IOError as e:
        print("ERROR: Oh dear... %s does not seem readable" % config_file)
        sys.exit(2)

    config_cmd = ['/usr/bin/env', 'php', '%s/config_to_json.php' % install_dir]
    try:
        proc = subprocess.Popen(config_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    except:
        print("ERROR: Could not execute: %s" % config_cmd)
        sys.exit(2)
    return proc.communicate()[0]


def db_open(server, database, username, password, port=0):
    try:
        if port == 0:
            db = MySQLdb.connect(host=server, user=username, passwd=password, db=database)
        else:
            db = MySQLdb.connect(host=server, port=port, user=username, passwd=password, db=database)
        return db
    except:
        print("ERROR: Could not connect to MySQL database!")
        sys.exit(2)


def main(oxidized_username, path_to_token_file, path_to_oxidized):
    try:
        config = json.loads(get_config_data())
    except:
        print("ERROR: Could not load or parse configuration, are PATHs correct?")
        sys.exit(2)

    # Create user in librenms
    # TODO Need to randomise the password for security
    subprocess.call(['php', '/opt/librenms/adduser.php', oxidized_username, 'oxidized', '10'])

    db_username = config['db_user']
    db_password = config['db_pass']
    db_port = int(config['db_port'])
    if config['db_host'][:5].lower() == 'unix:':
        db_server = config['db_host']
        db_port = 0
    elif config['db_socket']:
        db_server = config['db_socket']
        db_port = 0
    else:
        db_server = config['db_host']
    db_dbname = config['db_name']

    # https://stackoverflow.com/questions/976577/random-hash-in-python
    token = binascii.hexlify(os.urandom(16))
    query = "INSERT INTO api_tokens SET user_id=(SELECT user_id FROM users WHERE username='{}'), token_hash='{}', \
description='Oxidized'".format(oxidized_username, token)
    # Do actual work of putting token into the mySQL DB
    db = db_open(server=db_server, database=db_dbname, username=db_username, password=db_password, port=db_port)
    cursor = db.cursor()
    try:
        # Execute the SQL command
        cursor.execute(query)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    db.close()

    # Write token to file
    if path_to_token_file:
        directory, filename = os.path.split(os.path.abspath(path_to_token_file))
        # If directory does not exist.  Create it
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as exc:  # Python >2.5
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else:
                    raise

        # Write the file
        with open(path_to_token_file, "w") as token_fh:
            token_fh.write(token)

    # Write the token to the oxidized config file
    if path_to_oxidized:
        if not os.path.exists(path_to_oxidized):
            print("ERROR: Oxidiezed dir specified does not exits")
            sys.exit()

        # Read in the Oxidized config file
        with open('{}/config'.format(path_to_oxidized), 'r') as file_handler:
            oxidized_config = file_handler.read()

        # Put API token into config
        lst_oxidized_config_lines = oxidized_config.splitlines()
        for line in lst_oxidized_config_lines:
            if 'X-Auth-Token:' not in line:
                continue
            line = "X-Auth-Token: '{}'".format(token)

        # Write config file
        with open('{}/config'.format(path_to_oxidized), 'w') as file_handler:
            file_handler.write('\n'.join(lst_oxidized_config_lines))


if __name__ == '__main__':
    # Get commandline args and put into variables
    commandLineArgumentParser = argparse.ArgumentParser()
    commandLineArgumentParser.add_argument("oxidized_username", help="Oxidized username", type=str)
    commandLineArgumentParser.add_argument('-t', '--token', dest='token_file', type=str, default='',
                                           help='File to write API token to.  For use with Docker containers')
    commandLineArgumentParser.add_argument('-o', '--oxidized', dest='path_to_oxidized', type=str, default='',
                                           help='Location of Oxidized install')
    args = commandLineArgumentParser.parse_args()
    main(args.oxidized_username, args.token_file, args.path_to_oxidized)
