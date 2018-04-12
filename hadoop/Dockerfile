FROM ubuntu:16.04
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

# Update de system

RUN apt-get update
RUN apt-get install -y  apt-utils
RUN apt-get -y upgrade
RUN apt-get -y install build-essential 
RUN apt-get -y install \
	openjdk-8-jre \
	libssl-dev \
	tar \
	curl \
	wich \
	tar \
	sudo \
	rsync \
	nano \
	ssh \
	rsync \
	net-tools \
	python3
	

RUN apt-get update
RUN apt-get -y upgrade

##########################################

# Add files to directory /opt/bd

RUN mkdir /opt/bd

ADD bootstrap.sh /etc/bootstrap.sh
ADD HADOOP_KEYS /opt/bd
ADD hadoop-3.1.0.tar.gz /opt/bd/hadoop-3.1.0.tar.gz
RUN chown root:root /etc/bootstrap.sh
RUN chmod a+rwx /etc/bootstrap.sh
# Descomprimimos el tar de hadoop
RUN tar xvzf /opt/bd/hadoop-3.1.0.tar.gz -C /opt/bd
RUN rm hadoop-3.1.0.tar.gz
RUN ln -s hadoop-3.1.0 hadoop

##########################################


# Set envairoment variables

# hadoop
ENV HADOOP_PREFIX /opt/bd/hadoop
ENV HADOOP_COMMON_HOME /opt/bd/hadoop
ENV HADOOP_HDFS_HOME /opt/bd/hadoop
ENV HADOOP_MAPRED_HOME /opt/bd/hadoop
ENV HADOOP_YARN_HOME /opt/bd/hadoop
ENV HADOOP_CONF_DIR /opt/bd/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop

#Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64 

#bootstrap
ENV BOOTSTRAP /etc/bootstrap.sh

##########################################

# Add users and permision to hadoop

RUN groupadd -r hadoop && \
	useradd -r -g hadoop -d /opt/bd -s /bin/bash hdmaster && \
	chown -R hdmaster:hadoop /opt/bd



CMD ["/etc/bootstrap.sh", "-d"]
