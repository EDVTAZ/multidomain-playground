# Nginx Dockerfile
FROM nginx:1.19-alpine

# Install certbot for letsencrypt certificates
# Install also an init handler for alpine cron
RUN apk add --no-cache openrc busybox-initscripts

# Replace existing files by our own configs
RUN rm /etc/nginx/nginx.conf && rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/
COPY ./conf.d/flask_app.conf /etc/nginx/conf.d/

# We use a small hack with envsubst to pass variables to our Nginx config file.
# The variables in Nginx needs to be in this specific format: ${FOO}. That's why
# we create also a DOLLAR variable to add the "real" $ in our config flask_app.conf
# ex: $host needs to be set as ${DOLLAR}host
ARG DOMAINS
ARG FLASK

ENV DOMAINS=$DOMAINS
ENV FLASK=$FLASK
ENV DOLLAR='$'

# Substitute contents and write a new application.conf file, which is imported
# by nginx.conf
RUN envsubst \
      </etc/nginx/conf.d/flask_app.conf \
      >/etc/nginx/conf.d/application.conf \
  && rm /etc/nginx/conf.d/flask_app.conf

# App entrypoint and auto-renewal scripts
COPY ./bin/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install certificates and launch
ENTRYPOINT ../entrypoint.sh 