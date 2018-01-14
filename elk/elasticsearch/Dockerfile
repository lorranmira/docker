# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.1.1

# Alliedtelesis custom config
# ====
COPY ./config/ /usr/share/elasticsearch/config
# ====

# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu


VOLUME ["/usr/share/elasticsearch/logs"]