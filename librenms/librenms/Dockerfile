# https://github.com/jarischaefer/docker-librenms
FROM jarischaefer/docker-librenms

COPY files/ /

# Pull down the wait-for-it.sh
# Used to make sure DB is up when librenms container starts
RUN git clone https://github.com/vishnubob/wait-for-it.git /tmp/token/wait-for-it