# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash-oss:6.1.1

# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json

# Alliedtelesis custom config
# ====
RUN rm -f /usr/share/logstash/pipeline/logstash.conf

RUN mkdir -p /usr/share/logstash/logs \
    && chown -R logstash:logstash /usr/share/logstash/logs

COPY ./pipeline/ /usr/share/logstash/pipeline

COPY ./config/ /usr/share/logstash/config
# ====

VOLUME ["/usr/share/logstash/logs"]