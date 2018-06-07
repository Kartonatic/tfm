FROM karton91/ubuntu_base:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

####################################################################################
# HADOOP
# Hadoop file
ADD hadoop-2.7.6.tar.gz /opt/bd/hadoop-2.7.6.tar.gz
# El tar.gz se descomprime con el ADD por lo que solo tenemos que mover el directorio

# Add files to directory /opt/bd

RUN cd /opt/bd && \
	cp -R hadoop-2.7.6.tar.gz/hadoop-2.7.6 hadoop-2.7.6 && \
	rm -R hadoop-2.7.6.tar.gz && \
	ln -s hadoop-2.7.6 hadoop && \
	chown -R hdmaster:hadoop /opt/bd

ADD Default_Conf/hadoop2.7.6/* /opt/bd/hadoop/etc/hadoop/
RUN chown -R hdmaster:hadoop /opt/bd/hadoop/etc/hadoop/

####################################################################################

# IMPORTANT: if you don't use my yml file, you have to change entrypoint.sh or /etc/hosts
# Add routes yml for hosts
#ADD  Default_Conf/AddHosts /

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

####################################################################################
# Set envairoment variables
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

RUN 	echo export HADOOP_HOME=/opt/bd/hadoop  >> /opt/bd/.bashrc &&\
	echo export HADOOP_COMMON_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export HADOOP_HDFS_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export HADOOP_MAPRED_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export HADOOP_YARN_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export HADOOP_CONF_DIR=/opt/bd/hadoop/etc/hadoop >> /opt/bd/.bashrc &&\
	echo export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop >> /opt/bd/.bashrc &&\
	echo export PATH='$PATH':$HADOOP_HOME/bin >> /opt/bd/.bashrc



####################################################################################

# Create dir for the data in HDFS (NameNode, DataNodes y Checkpoint node) 
# and the log files. The owner have to be hdmaster.

RUN mkdir -p /var/data/hadoop/hdfs/nn /var/data/hadoop/hdfs/cpn /var/data/hadoop/hdfs/dn /var/log/hadoop/yarn /var/log/hadoop/hdfs /var/log/hadoop/mapred && \
	chown -R hdmaster:hadoop /var/data/hadoop/ &&\
	chown -R hdmaster:hadoop /var/log/hadoop

# Add volume for hdfs persistant
VOLUME /var/data/hadoop/hdfs
VOLUME /var/log/hadoop/

#Create user hdfs
RUN mkdir /home/hdfs &&\
    useradd -r -d /home/hdfs -s /bin/bash hdfs &&\
    cp /opt/bd/.bash_logout /home/hdfs/ &&\
    cp /opt/bd/.profile /home/hdfs/ &&\
    cp /opt/bd/.bashrc /home/hdfs/ &&\
    chown -R hdfs /home/hdfs &&\
    pip3 install pymongo

# Based on:
# https://github.com/sequenceiq/hadoop-docker 
# https://github.com/big-data-europe/docker-hadoop
# and my own knowledge