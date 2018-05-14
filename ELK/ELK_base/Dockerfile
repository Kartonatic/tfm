FROM karton91/ubuntu_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

####################################################################################
# Add user for elasticsearch and directories for it

RUN mkdir -p /opt/bd/elastic && \
	groupadd -r bbdd  && \
	useradd -r -g bbdd -d /opt/bd/elastic -s /bin/bash elastic && \
	chown -R elastic:bbdd /opt/bd/elastic/ 
####################################################################################
# SSH

RUN cp -R ~/.ssh /opt/bd/elastic/.ssh && chown -R elastic:bbdd /opt/bd/elastic/.ssh && \
    chown -R elastic:bbdd /opt/bd/elastic/.ssh

# BASH

RUN cp /etc/skel/.bash_logout /opt/bd/elastic/ && \ 
	cp /etc/skel/.profile /opt/bd/elastic/ && \
	cp /etc/skel/.bashrc /opt/bd/elastic/  && \
	chown -R elastic:bbdd /opt/bd/elastic/.bash_logout && \
	chown -R elastic:bbdd /opt/bd/elastic/.profile && \
	chown -R elastic:bbdd /opt/bd/elastic/.bashrc

####################################################################################
# Download and install elasticsearch, logstash and kibana

ADD elasticsearch-6.2.4.tar.gz /opt/bd/elastic/elasticsearch-6.2.4.tar.gz 
ADD kibana-6.2.4-linux-x86_64.tar.gz /opt/bd/elastic/kibana-6.2.4-linux-x86_64.tar.gz
ADD logstash-6.2.4.tar.gz /opt/bd/elastic/logstash-6.2.4.tar.gz

RUN cd /opt/bd/elastic && \
	cp -R elasticsearch-6.2.4.tar.gz/elasticsearch-6.2.4 elasticsearch-6.2.4 && \
	rm -R elasticsearch-6.2.4.tar.gz && \
	ln -s elasticsearch-6.2.4 elasticsearch && \
	cp -R kibana-6.2.4-linux-x86_64.tar.gz/kibana-6.2.4-linux-x86_64 kibana-6.2.4-linux-x86_64 && \
	rm -R kibana-6.2.4-linux-x86_64.tar.gz && \
	ln -s kibana-6.2.4-linux-x86_64 kibana && \
	cp -R logstash-6.2.4.tar.gz/logstash-6.2.4 logstash-6.2.4 && \
	rm -R logstash-6.2.4.tar.gz && \
	ln -s logstash-6.2.4 logstash && \
	chown -R elastic:bbdd /opt/bd/elastic/ && \
	chown -R elastic:bbdd /opt/bd/elastic/ 

####################################################################################
#Add configurations and enviroment variables

ADD Default_Conf/elastic_conf/config /opt/bd/elastic/elasticsearch/config
ADD Default_Conf/kibana_conf/config /opt/bd/elastic/kibana/config
ADD Default_Conf/logstash_conf/config /opt/bd/elastic/logstash/config

RUN chown -R elastic:bbdd /opt/bd/elastic/elasticsearch/config && \
    chown -R elastic:bbdd /opt/bd/elastic/kibana/config && \
    chown -R elastic:bbdd /opt/bd/elastic/logstash/config && \
    mkdir -p /var/data/elastic && \
    chown -R elastic:bbdd /var/data/elastic && \
    mkdir -p /var/log/elastic && \
    chown -R elastic:bbdd /var/log/elastic && \
    mkdir -p /var/data/elastic/elasticsearch && \
    chown -R elastic:bbdd /var/data/elastic/elasticsearch && \
    mkdir -p /var/data/elastic/kibana && \
    chown -R elastic:bbdd /var/data/elastic/kibana && \
    mkdir -p /var/data/elastic/logstash && \
    chown -R elastic:bbdd /var/data/elastic/logstash && \
    mkdir -p /var/log/elastic/elasticsearch && \
    chown -R elastic:bbdd /var/log/elastic/elasticsearch && \
    mkdir -p /var/log/elastic/kibana && \
    chown -R elastic:bbdd /var/log/elastic/kibana && \
    mkdir -p /var/log/elastic/logstash && \
    chown -R elastic:bbdd /var/log/elastic/logstash


VOLUME /var/data/elastic/elasticsearch
VOLUME /var/log/elastic/elasticsearch

VOLUME /var/data/elastic/kibana
VOLUME /var/log/elastic/kibana

VOLUME /var/data/elastic/logstash
VOLUME /var/log/elastic/logstash

ENV ES_HOME /opt/bd/elastic/elasticsearch/
ENV KIBANA_HOME /opt/bd/elastic/kibana/
ENV LOGSTASH_HOME /opt/bd/elastic/logstash/
ENV ES_PATH_CONF /opt/bd/elastic/elasticsearch/config
ENV PATH /opt/bd/elastic/elasticsearch/bin:/opt/bd/elastic/kibana/bin:/opt/bd/elastic/logstash/bin:$PATH

RUN echo export ES_HOME=/opt/bd/elastic/elasticsearch/ >> /opt/bd/elastic/.bashrc && \
    echo export KIBANA_HOME=/opt/bd/elastic/kibana/ >> /opt/bd/elastic/.bashrc && \
    echo export LOGSTASH_HOME=/opt/bd/elastic/logstash/ >> /opt/bd/elastic/.bashrc && \
    echo export ES_PATH_CONF=/opt/bd/elastic/elasticsearch/config  >> /opt/bd/elastic/.bashrc && \
    echo export PATH=/opt/bd/elastic/elasticsearch/bin:/opt/bd/elastic/kibana/bin:/opt/bd/elastic/logstash/bin:'$PATH'  >> /opt/bd/elastic/.bashrc 

ADD Default_Conf/AddHostsELK /
RUN cat /AddHostsELK >> /AddHosts && \ 
    rm /AddHostsELK

EXPOSE 9200 9300 5601

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
