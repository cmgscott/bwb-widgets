FROM python:3.7.4-slim-buster
MAINTAINER Christin Scott (scottchristin(AT)gmail(DOT)com)
RUN apt-get update && \
    apt-get -y install python3-pip && \
    pip install --upgrade pip virtualenv setuptools GEOparse

COPY Program /root/Program