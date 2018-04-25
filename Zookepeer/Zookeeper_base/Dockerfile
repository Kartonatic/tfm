FROM karton91/hadoop_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root



ADD zookeeper-3.4.10.tar.gz /opt/zookeeper-3.4.10.tar.gz

RUN cd /opt && ls 

RUN cd /opt && \
	cp -R zookeeper-3.4.10.tar.gz/zookeeper-3.4.10 zookeeper-3.4.10 && \
	rm -R zookeeper-3.4.10.tar.gz && \
	ln -s zookeeper-3.4.10.tar.gz zookeeper


