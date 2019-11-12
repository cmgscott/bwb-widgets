FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install kwrite && \
    su - && \
    apt-get -y install sudo && \
    usermod -aG sudo root