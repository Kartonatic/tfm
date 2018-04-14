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
	curl \
	sudo \
	rsync \
	nano \
	ssh \
	rsync \
	net-tools \
	python3

RUN apt-get update
RUN apt-get -y upgrade

####################################################################################
# Add users for hadoop and directories for hadoop

RUN mkdir /opt/bd

RUN groupadd -r hadoop  && \
	useradd -r -g hadoop -d /opt/bd -s /bin/bash hdmaster

RUN chown -R hdmaster:hadoop /opt/bd

####################################################################################

# HADOOP

# Hadoop_keys

ADD HADOOP_KEYS /opt/bd


# Hadoop file
ADD hadoop-3.1.0.tar.gz /opt/bd/hadoop-3.1.0.tar.gz
# El tar.gz se descomprime con el ADD por lo que solo tenemos que mover el directorio

# Add files to directory /opt/bd

RUN cd /opt/bd && \
	cp -R hadoop-3.1.0.tar.gz/hadoop-3.1.0 hadoop-3.1.0 && \
	rm -R hadoop-3.1.0.tar.gz && \
	ln -s hadoop-3.1.0 hadoop

ADD Default_Conf/hadoop/* /opt/bd/hadoop/etc/hadoop/
RUN echo 'Please wait to change permisions...'
RUN chown -R hdmaster:hadoop /opt/bd


####################################################################################

# ssh configuration

# ssh config file (SET StrictHostKeyChecking “no”)
ADD Default_Conf/ssh_config /etc/ssh/ssh_config

# OPEN SSH PORT AND ADD ssh key

EXPOSE 22

# Podemos crear nuestra propia rsa key o agregar alguna que tengamos preparda

# OPCION 1: GENERARLA DE FORMA AUTOMATICA RSA_KEY
# OPCION 1: Automatic rsa_key
 RUN sudo su hdmaster && \
 	mkdir ~/.ssh/ &&  \
 	cd ~/.ssh/ \ &&  \
 	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
 	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
 	chmod 644 ~/.ssh/authorized_keys 

RUN chown -R hdmaster:hadoop /root/.ssh
RUN cp -R ~/ /opt/bd/.ssh && chown -R hdmaster:hadoop /opt/bd/.ssh


# OPCION 2: TENER NUESTRA PROPIA RSA_KEY
# nos proporciona la ventaja de poder usar nuestro equipo como parte del cluster
# ya que podemos añadir las claves
# OPCION 2: Manual rsa_key
# RUN mkdir ~/.ssh/
# ADD .ssh/* /root/.ssh/
# RUN chmod 644 ~/.ssh/autorized_keys


# ESTO NO VALE DE NADA PORQUE NO SE HA CONSTRUIDO LA MAQUINA REAL
# This not run because it's not a real machine
# RUN service ssh start
# RUN sudo su hdmaster && cd ~/ && ssh localhost

####################################################################################

# Add bootstrap

ADD bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod a+rwx /etc/bootstrap.sh

####################################################################################


# Set envairoment variables

ENV JAVA_VERSION 8

#Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64 


# Version
ENV HADOOP_VERSION 3.1.0

# Hadoop

ENV HADOOP_PREFIX /opt/bd/hadoop
ENV HADOOP_COMMON_HOME /opt/bd/hadoop
ENV HADOOP_HDFS_HOME /opt/bd/hadoop
ENV HADOOP_MAPRED_HOME /opt/bd/hadoop
ENV HADOOP_YARN_HOME /opt/bd/hadoop
ENV HADOOP_CONF_DIR /opt/bd/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV PATH=$PATH:$HADOOP_PREFIX/bin


#bootstrap
ENV BOOTSTRAP /etc/bootstrap.sh

####################################################################################

# Create dir for the data in HDFS (NameNode, DataNodes y Checkpoint node) 
# and the log files. The owner have to be hdmaster.

RUN mkdir -p /var/data/hadoop/hdfs/nn
RUN mkdir -p /var/data/hadoop/hdfs/cpn
RUN mkdir -p /var/data/hadoop/hdfs/dn 
RUN chown -R hdmaster:hadoop /var/data/hadoop/hdfs
RUN mkdir -p /var/log/hadoop/yarn
RUN mkdir -p /var/log/hadoop/hdfs
RUN mkdir -p /var/log/hadoop/mapred
RUN chown -R hdmaster:hadoop /var/log/hadoop

RUN mkdir -p /hadoop/dfs/data
VOLUME /hadoop/dfs/data

CMD ["/etc/bootstrap.sh", "-d"]

# Based on:
# https://github.com/sequenceiq/hadoop-docker 
# https://github.com/big-data-europe/docker-hadoop
# and my own knowledge