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

# GENERATE rsa_key
RUN sudo su hdmaster && \
	mkdir ~/.ssh/ &&  \
	cd ~/.ssh/ \ &&  \
	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
	chmod 644 ~/.ssh/authorized_keys

RUN cp -R ~/.ssh /opt/bd/.ssh && chown -R hdmaster:hadoop /opt/bd/.ssh
RUN chown -R hdmaster:hadoop /opt/bd/.ssh
RUN chown -R root:root /root/.ssh/ root


# ESTO NO VALE DE NADA PORQUE NO SE HA CONSTRUIDO LA MAQUINA REAL
# This it not run because it's not a real machine
# RUN service ssh start
# RUN sudo su hdmaster && cd ~/ && ssh localhost

# IMPORTANT: if you don't use my yaml file, you have to change entrypoint.sh or /etc/hosts
# Add routes yml for hosts
ADD  Default_Conf/AddHosts /

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

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

ENV HADOOP_HOME /opt/bd/hadoop
ENV HADOOP_COMMON_HOME /opt/bd/hadoop
ENV HADOOP_HDFS_HOME /opt/bd/hadoop
ENV HADOOP_MAPRED_HOME /opt/bd/hadoop
ENV HADOOP_YARN_HOME /opt/bd/hadoop
ENV HADOOP_CONF_DIR /opt/bd/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

RUN cp /etc/skel/.bash_logout /opt/bd/
RUN cp /etc/skel/.profile /opt/bd/
RUN cp /etc/skel/.bashrc /opt/bd/
RUN echo export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /opt/bd/.bashrc
RUN echo export HADOOP_HOME=/opt/bd/hadoop  >> /opt/bd/.bashrc
RUN echo export PATH=$PATH:$HADOOP_HOME/bin >> /opt/bd/.bashrc

RUN chown -R hdmaster:hadoop /opt/bd/.bash_logout
RUN chown -R hdmaster:hadoop /opt/bd/.profile
RUN chown -R hdmaster:hadoop /opt/bd/.bashrc

#bootstrap
ENV BOOTSTRAP /etc/bootstrap.sh

####################################################################################

# Create dir for the data in HDFS (NameNode, DataNodes y Checkpoint node) 
# and the log files. The owner have to be hdmaster.

RUN mkdir -p /var/data/hadoop/hdfs/nn
RUN mkdir -p /var/data/hadoop/hdfs/cpn
RUN mkdir -p /var/data/hadoop/hdfs/dn 
RUN chown -R hdmaster:hadoop /var/data/hadoop/
RUN mkdir -p /var/log/hadoop/yarn
RUN mkdir -p /var/log/hadoop/hdfs
RUN mkdir -p /var/log/hadoop/mapred
RUN chown -R hdmaster:hadoop /var/log/hadoop

# Add volume for hdfs persistant
VOLUME /var/data/hadoop/hdfs

CMD ["/etc/bootstrap.sh", "-bash"]

# Based on:
# https://github.com/sequenceiq/hadoop-docker 
# https://github.com/big-data-europe/docker-hadoop
# and my own knowledge