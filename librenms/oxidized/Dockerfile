FROM oxidized/oxidized:latest
RUN apt update && apt install -y tzdata && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY files/oxidized /tmp/oxidized
COPY files/etc /etc