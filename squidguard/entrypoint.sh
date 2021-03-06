#!/bin/bash
set -e

echo "running squidGuard with WPAD_IP=${WPAD_IP} WPAD_NOPROXY_NET=${WPAD_NOPROXY_NET} WPAD_NOPROXY_MASK=${WPAD_NOPROXY_MASK}"

if [  "${WPAD_IP}" != "" ]; then
    sed -i "s/{{WPAD_IP}}/${WPAD_IP}/" /var/www/html/wpad.dat
    sed -i "s/{{WPAD_NOPROXY_NET}}/${WPAD_NOPROXY_NET}/" /var/www/html/wpad.dat
    sed -i "s/{{WPAD_NOPROXY_MASK}}/${WPAD_NOPROXY_MASK}/" /var/www/html/wpad.dat
fi

# start apache to serve block.html wpad.dat file
sudo /etc/init.d/apache2 restart

# run original squid start script
exec /sbin/entrypoint_pre_squidguard.sh
