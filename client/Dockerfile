FROM mcr.microsoft.com/playwright/python:v1.37.0-jammy

RUN apt update && apt install libnss3-tools
RUN python -m pip install playwright                                       # https://github.com/microsoft/playwright-python/issues/1978
RUN curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64" && \ 
    chmod +x mkcert-v*-linux-amd64 && \
    cp mkcert-v*-linux-amd64 /usr/local/bin/mkcert

ARG DOMAINS
RUN mkdir -p /root/.pki/nssdb && certutil -d /root/.pki/nssdb -N           # https://github.com/microsoft/playwright/issues/4785#issuecomment-1611417285
RUN mkcert -install -ecdsa $DOMAINS

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 
ENTRYPOINT /entrypoint.sh
