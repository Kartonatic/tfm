FROM karton91/ubuntu_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

####################################################################################
# Add user for zookeeper and directories for zookeper

RUN mkdir /opt/orchestrator &&  groupadd -r zk &&\
	useradd -r -g zk -d /opt/orchestrator -s /bin/bash zkmaster && \
	chown -R zkmaster:zk /opt/orchestrator/

####################################################################################
# SSH

RUN cp -R ~/.ssh /opt/orchestrator/.ssh && chown -R zkmaster:zk /opt/orchestrator/.ssh && \
    chown -R zkmaster:zk /opt/orchestrator/.ssh

####################################################################################

# ADD ZOOKEEPER AND CONFIGURATION

ADD zookeeper-3.4.10.tar.gz /opt/orchestrator/zookeeper-3.4.10.tar.gz

RUN cd /opt/orchestrator/ && \
	cp -R zookeeper-3.4.10.tar.gz/zookeeper-3.4.10 zookeeper-3.4.10 && \
	rm -R zookeeper-3.4.10.tar.gz && \
	ln -s zookeeper-3.4.10 zookeeper && \
	chown -R zkmaster:zk /opt/orchestrator/zookeeper && \
	chown -R zkmaster:zk /opt/orchestrator/zookeeper/ 

# Configuration

ADD Default_Conf/zoo.cfg /opt/orchestrator/zookeeper/conf/zoo.cfg
ADD Default_Conf/zoo_replicated.cfg.dynamic /opt/orchestrator/zookeeper/conf/zoo_replicated.cfg.dynamic

RUN chown -R zkmaster:zk /opt/orchestrator/zookeeper/conf/ && \
    mkdir -p /var/data/zookeeper && \
    mkdir -p /var/log/zookeeper && \
    chown -R zkmaster:zk /var/log/zookeeper && \
    chown -R zkmaster:zk /var/data/zookeeper

VOLUME /var/log/zookeeper
VOLUME /var/data/zookeeper

####################################################################################

ENV ZOOKEEPER_HOME /opt/orchestrator/zookeeper/
ENV ZOOBINDIR /opt/orchestrator/zookeeper/bin
ENV ZOOCFGDIR /opt/orchestrator/zookeeper/conf

RUN cp /etc/skel/.bash_logout /opt/orchestrator/ && \
	cp /etc/skel/.profile /opt/orchestrator/ && \
	cp /etc/skel/.bashrc /opt/orchestrator/ && \
	echo export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /opt/orchestrator/.bashrc  && \
	echo export ZOOKEEPER_HOME=/opt/orchestrator/zookeeper >> /opt/orchestrator/.bashrc  && \
	echo export ZOOBINDIR=/opt/orchestrator/zookeeper/bin >> /opt/orchestrator/.bashrc  && \
	echo export ZOOCFGDIR=/opt/orchestrator/zookeeper/conf >> /opt/orchestrator/.bashrc && \
	echo export PATH='$PATH':$ZOOKEEPER_HOME/bin >> /opt/orchestrator/.bashrc && \
	chown -R zkmaster:zk /opt/orchestrator/.bash_logout && \
	chown -R zkmaster:zk /opt/orchestrator/.profile && \
	chown -R zkmaster:zk /opt/orchestrator/.bashrc 

ADD Default_Conf/AddZooKeeperHost /
RUN cat /AddZooKeeperHost >> /AddHosts  && rm /AddZooKeeperHost

# Expose client port (2188/tcp), peer connection port (2888/tcp), leader election port (3888/tcp)
EXPOSE 2181 2888 3888

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]


#BASED ON
# https://zookeeper.apache.org/ (official website) 
# https://github.com/31z4/zookeeper-docker
# https://github.com/confluentinc/docker-images
# and my own knowledge