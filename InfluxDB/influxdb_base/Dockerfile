FROM karton91/ubuntu_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

####################################################################################
# Add user for influxdb and directories for it

RUN mkdir -p /opt/bd/influxdb && \
	groupadd -r influxdb  && \
	useradd -r -g influxdb -d /opt/bd/influxdb -s /bin/bash influxdb && \
	chown -R influxdb:influxdb /opt/bd/influxdb/
	
####################################################################################
# SSH

RUN cp -R ~/.ssh /opt/bd/influxdb/.ssh && chown -R influxdb:influxdb /opt/bd/influxdb/.ssh && \
    chown -R influxdb:influxdb /opt/bd/influxdb/.ssh

# BASH

RUN cp /etc/skel/.bash_logout /opt/bd/influxdb/ && \ 
	cp /etc/skel/.profile /opt/bd/influxdb/ && \
	cp /etc/skel/.bashrc /opt/bd/influxdb/  && \
	chown -R influxdb:influxdb /opt/bd/influxdb/.bash_logout && \
	chown -R influxdb:influxdb /opt/bd/influxdb/.profile && \
	chown -R influxdb:influxdb /opt/bd/influxdb/.bashrc

####################################################################################

# Download and install influxdb, kapacitor, chronograf and telegraf

ADD influxdb-1.5.2_linux_amd64.tar.gz /opt/bd/influxdb/influxdb-1.5.2_linux_amd64.tar.gz 
ADD kapacitor-1.4.1_linux_amd64.tar.gz /opt/bd/influxdb/kapacitor-1.4.1_linux_amd64.tar.gz
ADD chronograf-1.4.4.2_linux_amd64.tar.gz /opt/bd/influxdb/chronograf-1.4.4.2_linux_amd64.tar.gz
ADD telegraf-1.6.2_linux_amd64.tar.gz /opt/bd/influxdb/telegraf-1.6.2_linux_amd64.tar.gz


RUN cd /opt/bd/influxdb && \
	cp -R influxdb-1.5.2_linux_amd64.tar.gz/./influxdb-1.5.2-1 influxdb-1.5.2 && \
	rm -R influxdb-1.5.2_linux_amd64.tar.gz && \
	ln -s influxdb-1.5.2 influxdb && \
	cp -R kapacitor-1.4.1_linux_amd64.tar.gz/./kapacitor-1.4.1-1 kapacitor-1.4.1 && \
	rm -R kapacitor-1.4.1_linux_amd64.tar.gz && \
	ln -s kapacitor-1.4.1 kapacitor && \
	cp -R chronograf-1.4.4.2_linux_amd64.tar.gz/./chronograf-1.4.4.2-1 chronograf-1.4.4.2 && \
	rm -R chronograf-1.4.4.2_linux_amd64.tar.gz && \
	ln -s chronograf-1.4.4.2 chronograf && \
	cp -R telegraf-1.6.2_linux_amd64.tar.gz/./telegraf telegraf-1.6.2 && \
	rm -R telegraf-1.6.2_linux_amd64.tar.gz && \
	ln -s telegraf-1.6.2 telegraf && \
	chown -R influxdb:influxdb /opt/bd/influxdb/ && \
	chown -R influxdb:influxdb /opt/bd/influxdb/ 

####################################################################################

#Add configurations and enviroment variables

ADD Default_Conf/influxdb.conf /opt/bd/influxdb/influxdb/etc/influxdb/influxdb.conf
ADD Default_Conf/telegraf.conf /opt/bd/influxdb/telegraf/etc/telegraf/telegraf.conf
ADD Default_Conf/kapacitor.conf /opt/bd/influxdb/kapacitor/etc/kapacitor/kapacitor.conf

ENV INFLUXDB_HOME /opt/bd/influxdb/influxdb/
ENV KAPACITOR_HOME /opt/bd/influxdb/kapacitor/
ENV CHRONOGRAF_HOME /opt/bd/influxdb/chronograf/
ENV TELEGRAF_HOME /opt/bd/influxdb/telegraf/

RUN 	echo export INFLUXDB_HOME=/opt/bd/hadoop  >> /opt/bd/.bashrc &&\
	echo export KAPACITOR_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export CHRONOGRAF_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export TELEGRAF_HOME=/opt/bd/hadoop >> /opt/bd/.bashrc &&\
	echo export PATH='$PATH':$INFLUXDB_HOME/usr/bin/:$KAPACITOR_HOME/usr/bin/:$CHRONOGRAF_HOME/usr/bin/:$TELEGRAF_HOME/usr/bin/ >> /opt/bd/influxdb/.bashrc

RUN chown -R influxdb:influxdb /opt/bd/influxdb/influxdb/etc/influxdb/influxdb.conf /opt/bd/influxdb/telegraf/etc/telegraf/telegraf.conf /opt/bd/influxdb/kapacitor/etc/kapacitor/kapacitor.conf && \
    mkdir -p /var/data/influxdb && \
    mkdir -p /var/log/influxdb && \
    chown -R influxdb:influxdb /var/data/influxdb && \
    chown -R influxdb:influxdb /var/log/influxdb


ADD Default_Conf/AddHostsInflux /
RUN cat /AddHostsInflux >> /AddHosts
RUN rm /AddHostsInflux

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]