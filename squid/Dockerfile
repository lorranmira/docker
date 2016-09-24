FROM phusion/baseimage:0.9.19

ENV SQUID_CACHE_DIR=/var/spool/squid \
    SQUID_LOG_DIR=/var/log/squid \
    SQUID_USER=proxy \
    LOCAL_NETWORK="10.1.1.0/24"

RUN apt-get -q update \
    && apt-get -qy --no-install-recommends install squid \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mv /etc/squid/squid.conf /etc/squid/squid.conf.dist

COPY squid.conf /etc/squid/squid.conf

RUN sed -i "s:^#acl localnet src 10.0.0.0/8:acl localnet src ${LOCAL_NETWORK}:" /etc/squid/squid.conf \
    && sed -i "s/^#http_access allow localnet/http_access allow localnet/" /etc/squid/squid.conf \
    && sed -i "s/^cache_dir ufs/cache_dir aufs/" /etc/squid/squid.conf

RUN sed -i "s/^su root syslog/#su root syslog/" /etc/logrotate.conf
#RUN sed -i "s:/usr/sbin/squid3 -k rotate:kill -SIGHUP 1:" /etc/logrotate.d/squid

RUN mkdir /etc/service/squid
COPY entrypoint.sh /etc/service/squid/run
RUN chmod 755 /etc/service/squid/run

EXPOSE 3128/tcp
VOLUME ["${SQUID_CACHE_DIR}", "${SQUID_LOG_DIR}"]

CMD ["/sbin/my_init"]
