FROM debian:jessie

ENV SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy

RUN apt-get -q update \
    && apt-get -qy --no-install-recommends install squid3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i "s/^#acl localnet/acl localnet/" /etc/squid3/squid.conf \
    && sed -i "s/^#http_access allow localnet/http_access allow localnet/" /etc/squid3/squid.conf \
    && mkdir -p /var/cache/squid3 \
    && chown -R proxy:proxy /var/cache/squid3

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 3128/tcp
VOLUME ["${SQUID_CACHE_DIR}", "/etc/squid3"]
ENTRYPOINT ["/sbin/entrypoint.sh"]
