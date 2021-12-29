#!/bin/sh
gunicorn -w 4 --threads 2 app:app
#gunicorn --certfile=tls/cert.pem --keyfile=tls/key.pem -w 4 --threads 2  --bind 0.0.0.0:443 app:app