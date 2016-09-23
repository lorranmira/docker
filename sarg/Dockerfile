FROM squidguard

ENV SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy \
    LOCAL_NETWORK="10.1.1.0/24"

RUN apt-get -q update \
    && apt-get -qy --no-install-recommends install sarg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mv /etc/sarg/sarg.conf /etc/sarg/sarg.conf.dist \
    && mv /sbin/entrypoint.sh /sbin/entrypoint_pre_sarg.sh

COPY sarg.conf /etc/sarg/sarg.conf
COPY sarg_apache.conf /etc/apache2/conf-available/sarg.conf
COPY entrypoint.sh /sbin/entrypoint.sh

RUN sed -i "s:^access_log /var/log/squid/access.log:access_log ${SQUID_LOG_DIR}/access.log:" /etc/sarg/sarg.conf \
    && sed -i "s:^#output_dir /var/www/html/squid-reports:output_dir /var/www/html/squid-reports:" /etc/sarg/sarg.conf \
    && sed -i "s:^output_dir /var/lib/sarg:#output_dir /var/lib/sarg:" /etc/sarg/sarg.conf \
    && sed -i "s:^resolve_ip:resolve_ip yes:" /etc/sarg/sarg.conf \
    && sed -i "s:^charset Latin1:charset UTF-8:" /etc/sarg/sarg.conf \
    && echo "127.0.0.1" >> /etc/sarg/exclude_hosts \
    && mkdir -p /var/www/html/squid-reports \
    && chmod a+x /sbin/entrypoint.sh

EXPOSE 3128 80
VOLUME ["/var/spool/squid3", "/var/log/squidguard", "/var/www/html/"]

CMD ["/sbin/entrypoint.sh"]