FROM python:3.7.4-slim-buster
MAINTAINER Christin Scott (scottchristin(AT)gmail(DOT)com)
RUN apt-get update && \
    apt-get -y install python3-pip && \
    apt-get -y install bash tar && \
    pip install --upgrade pip virtualenv setuptools GEOparse


#FROM python:3.7.4-slim-buster
#RUN apt-get update
##RUN apt-get -y install bash tar
#RUN apt-get install software-properties-common
#RUN add-apt-repository universe
#RUN apt-get -yqq install python3-setuptools
#RUN apt-get -y install python3-pip && \
#    pip install --upgrade pip virtualenv setuptools GEOparse

COPY download.sh /root
COPY download.py /root
