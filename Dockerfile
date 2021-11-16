# syntax=docker/dockerfile:1

# pull base image
FROM python:3

# set app home dir
ENV APP_HOME=/app
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . $APP_HOME

ENTRYPOINT ["./gunicorn.sh"]