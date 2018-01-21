#! /usr/bin/env python2
try:

    import json
    import os
    import subprocess
    import sys
    import binascii

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


install_dir = os.path.dirname(os.path.realpath(__file__))
config_file = install_dir + '/config.php'


# Fetch configuration details from the config_to_json.php script
def get_config_data():
    config_cmd = ['/usr/bin/env', 'php', '%s/config_to_json.php' % install_dir]
    try:
        proc = subprocess.Popen(config_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    except:
        print("ERROR: Could not execute: %s" % config_cmd)
        sys.exit(2)
    return proc.communicate()[0]


def db_open():
    try:
        if db_port == 0:
            db = MySQLdb.connect(host=db_server, user=db_username, passwd=db_password, db=db_dbname)
        else:
            db = MySQLdb.connect(host=db_server, port=db_port, user=db_username, passwd=db_password, db=db_dbname)
        return db
    except:
        print("ERROR: Could not connect to MySQL database!")
        sys.exit(2)

# Read in the environment variable required to set the oxidized username
try:
    oxidized_username = os.environ['OXIDIZED_USERNAME']
except:
    print("ERROR: Could not get the Oxidized username from environment")
    sys.exit(2)

try:
    with open(config_file) as f:
        pass
except IOError as e:
    print("ERROR: Oh dear... %s does not seem readable" % config_file)
    sys.exit(2)

try:
    config = json.loads(get_config_data())
except:
    print("ERROR: Could not load or parse configuration, are PATHs correct?")
    sys.exit(2)

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

# token = '90e0ae436b37320501e89774e9af9a69'
# https://stackoverflow.com/questions/976577/random-hash-in-python
token = binascii.hexlify(os.urandom(16))
query = "INSERT INTO api_tokens SET user_id=(SELECT user_id FROM users WHERE username='{}'), token_hash='{}', \
description='Oxidized'".format(oxidized_username, token)

# Do actual work of putting token into the mySQL DB
db = db_open()
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
