FROM mcr.microsoft.com/playwright/python

RUN curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64" && \ 
    chmod +x mkcert-v*-linux-amd64 && \
    cp mkcert-v*-linux-amd64 /usr/local/bin/mkcert

ARG DOMAINS
RUN mkcert -install -ecdsa $DOMAINS

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 
ENTRYPOINT /entrypoint.sh
