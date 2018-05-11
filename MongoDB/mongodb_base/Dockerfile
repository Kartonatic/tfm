FROM karton91/ubuntu_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

####################################################################################
# Add user for mongodb and directories for it

RUN mkdir -p /opt/bd/mongodb && \
	groupadd -r mongodb  && \
	useradd -r -g mongodb -d /opt/bd/mongodb -s /bin/bash mongodb && \
	chown -R mongodb:mongodb /opt/bd/mongodb/ && \
	apt-get install -y mongodb

#METER TODO AQUI

####################################################################################
# SSH

RUN cp -R ~/.ssh /opt/bd/mongodb/.ssh && chown -R mongodb:mongodb /opt/bd/mongodb/.ssh && \
    chown -R mongodb:mongodb /opt/bd/mongodb/.ssh

# BASH

RUN cp /etc/skel/.bash_logout /opt/bd/mongodb/ && \ 
	cp /etc/skel/.profile /opt/bd/mongodb/ && \
	cp /etc/skel/.bashrc /opt/bd/mongodb/  && \
	chown -R mongodb:mongodb /opt/bd/mongodb/.bash_logout && \
	chown -R mongodb:mongodb /opt/bd/mongodb/.profile && \
	chown -R mongodb:mongodb /opt/bd/mongodb/.bashrc

####################################################################################
#Add configurations and enviroment variables

ADD Default_Conf/mongodb.conf /etc/mongodb.conf

RUN chown -R mongodb:mongodb /etc/mongodb.conf && \
    mkdir -p /var/data/mongodb && \
    mkdir -p /var/log/mongodb && \
    chown -R mongodb:mongodb /var/data/mongodb && \
    chown -R mongodb:mongodb /var/log/mongodb


VOLUME /var/data/mongodb /var/log/mongodb

ADD Default_Conf/AddHostsMongo /
RUN cat /AddHostsMongo >> /AddHosts
RUN rm /AddHostsMongo

EXPOSE 27017

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
