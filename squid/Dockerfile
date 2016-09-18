FROM debian:jessie
RUN apt-get -q update && \
    apt-get -qy --no-install-recommends install squid3 curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN sed -i "s/^#acl localnet/acl localnet/" /etc/squid3/squid.conf \
    && sed -i "s/^#http_access allow localnet/http_access allow localnet/" /etc/squid3/squid.conf \
    && mkdir -p /var/cache/squid3 \
    && chown -R proxy:proxy /var/cache/squid3

EXPOSE 3128
VOLUME ["/var/spool/squid3"]

CMD ["/bin/bash"]
