#!/bin/bash
set -e

if [ ! -d "/var/www/html/squid-report" ]; then
    echo "Making dir [/var/www/html/squid-reports]"
    mkdir -p /var/www/html/squid-reports
fi

echo "running Sarg with LOCAL_NETWORK=${LOCAL_NETWORK}"

sed -i "s:{{LOCAL_NETWORK}}:${LOCAL_NETWORK}:" /etc/apache2/conf-available/sarg.conf

# Enable Sarg configuration
sudo a2enconf sarg

# restart apache to serve pages
sudo /etc/init.d/apache2 restart

# Generate initial reports
sudo /usr/bin/sarg

# run original squid start script
exec /sbin/entrypoint_pre_sarg.sh