FROM sebp/elk

# install syslog input plugin
WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-input-syslog

# overwrite existing file
ADD ./logstash/config/30-elasticsearch-output.conf /etc/logstash/conf.d/30-output.conf

# Move file from parent image
RUN mv /etc/logstash/conf.d/10-syslog.conf /etc/logstash/conf.d/10-syslog.conf.BAK

# add new files
COPY ./logstash/config/05-syslog-input.conf ./logstash/config/06-save-full-message.conf \
 ./logstash/config/10-syslog-filter.conf ./logstash/config/14-awplus-syslog-filter.conf \
 ./logstash/config/15-tq-syslog-filter.conf ./logstash/config/40-output-file.conf /etc/logstash/conf.d/

# Expose TCP ports
EXPOSE 514 5601 9200 9300 5044
