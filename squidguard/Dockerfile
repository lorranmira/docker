FROM squid_proxy

ENV SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy \
    WPAD_NOPROXY_NET="10.1.1.0/24" \
    WPAD_NOPROXY_MASK="255.255.255.0" \
    WPAD_IP="10.1.1.101"

RUN apt-get install -y squidguard apache2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN sudo echo 'AddType application/x-ns-proxy-autoconfig .dat' >> /etc/apache2/httpd.conf

RUN wget http://www.shallalist.de/Downloads/shallalist.tar.gz \
    && tar -xzf shallalist.tar.gz -C /var/lib/squidguard/db \
    && rm shallalist.tar.gz \
    && chown proxy:proxy /var/lib/squidguard/db -R \
    && echo "redirect_program /usr/bin/squidGuard -c /etc/squidguard/squidGuard.conf" >> /etc/squid3/squid.conf


COPY wpad.dat /var/www/html/wpad.dat
COPY block.html /var/www/html/block.html
COPY squidGuard.conf /etc/squidguard/squidGuard.conf
COPY startSquidGuard /startSquidGuard

RUN sudo chmod a+x /startSquidGuard

RUN sudo -u proxy squidGuard -C all

EXPOSE 3128 80
VOLUME ["/var/spool/squid3", "/var/log/squidguard", "/var/www/html/"]

CMD ["/startSquidGuard"]