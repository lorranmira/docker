FROM debian:jessie

ENV SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy \
    LOCAL_NETWORK="10.1.1.0/24"

RUN apt-get -q update \
    && apt-get -qy --no-install-recommends install squid3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mv /etc/squid3/squid.conf /etc/squid3/squid.conf.dist \
    && mkdir -p /var/cache/squid3 \
    && mkdir -p /config \
    && chown -R proxy:proxy /var/cache/squid3

COPY squid.conf /config/squid.conf

RUN ln -s /config/squid.conf /etc/squid3/squid.conf
    && chown -R proxy:proxy /config \

RUN sed -i "s:^#acl localnet src 10.0.0.0/8:acl localnet src ${LOCAL_NETWORK}:" /etc/squid3/squid.conf \
    && sed -i "s/^#http_access allow localnet/http_access allow localnet/" /etc/squid3/squid.conf \

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 3128/tcp
VOLUME ["${SQUID_CACHE_DIR}", "/config", "${SQUID_LOG_DIR}"]
ENTRYPOINT ["/sbin/entrypoint.sh"]
