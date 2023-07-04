#!/bin/sh

sleep 1
ls -la /shared
/usr/sbin/nginx -g "daemon off;"  # this is run in the foreground, so need to be last
