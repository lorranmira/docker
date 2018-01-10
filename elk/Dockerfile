FROM sebp/elk

# install syslog input plugin
WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-input-syslog

# overwrite existing file
ADD logstash/config/30-elasticsearch-output.conf /etc/logstash/conf.d/30-output.conf

# add new file
ADD logstash/config/05-syslog-input.conf /etc/logstash/conf.d/05-syslog-input.conf \
ADD logstash/config/06-save-full-message.conf /etc/logstash/conf.d/06-save-full-message.conf \
ADD logstash/config/10-syslog-filter.conf /etc/logstash/conf.d/10-syslog-filter.conf \
ADD logstash/config/14-awplus-syslog-filter.conf /etc/logstash/conf.d/14-awplus-syslog-filter.conf \
ADD logstash/config/15-tq-syslog-filter.conf /etc/logstash/conf.d/15-tq-syslog-filter.conf \
ADD logstash/config/40-output-file.conf /etc/logstash/conf.d/40-output-file.conf

EXPOSE 514 5601 9200 9300 5044
