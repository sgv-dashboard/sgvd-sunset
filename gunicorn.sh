#!/bin/sh
gunicorn app:app -w 2 --threads 2