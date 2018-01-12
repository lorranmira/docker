FROM sebp/elk

# install syslog input plugin
WORKDIR ${LOGSTASH_HOME}
RUN gosu logstash bin/logstash-plugin install logstash-input-syslog logstash-output-file

# Remove existing file
RUN rm -rf /etc/logstash/conf.d/30-output.conf

# Move file from parent image
RUN mv /etc/logstash/conf.d/10-syslog.conf /etc/logstash/conf.d/10-syslog.conf.BAK

# add new files
COPY ./logstash/config/ /etc/logstash/conf.d

# Expose TCP/UDP ports
EXPOSE 514 514/udp 5601 9200 9300 5044
