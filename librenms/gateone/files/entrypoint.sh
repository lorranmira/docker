#!/bin/bash -e

NO_DNS_HOSTS_FILE=/tmp/token/hosts.nodns

# Import hosts that are not in DNS
if [ -f "$NO_DNS_HOSTS_FILE" ]; then
	cat ${NO_DNS_HOSTS_FILE} >> /etc/hosts
fi

# Execute original gateone command
sh -c "/usr/local/bin/update_and_run_gateone --log_file_prefix=/gateone/logs/gateone.log"