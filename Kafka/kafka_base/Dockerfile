FROM karton91/zookeeper_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

####################################################################################
# Add user for kafka and directories for kafka

mkdir -p /opt/queuesmanager

RUN groupadd -r queues  && \
	useradd -r -g queues -d /opt/queuesmanager -s /bin/bash queuesmaster

RUN chown -R queuesmaster:queues /opt/queuesmanager/
####################################################################################
# SSH

RUN cp -R ~/.ssh /opt/queuesmanager/.ssh && chown -R queuesmaster:queues /opt/queuesmanager/.ssh
RUN chown -R queuesmaster:queues /opt/queuesmanager/.ssh

# BASH

RUN cp /etc/skel/.bash_logout /opt/queuesmanager/
RUN cp /etc/skel/.profile /opt/queuesmanager/
RUN cp /etc/skel/.bashrc /opt/queuesmanager/

RUN chown -R queuesmaster:queues /opt/queuesmanager/.bash_logout
RUN chown -R queuesmaster:queues /opt/queuesmanager/.profile
RUN chown -R queuesmaster:queues /opt/queuesmanager/.bashrc

####################################################################################
# Download and install kafka

ADD kafka_2.12-1.1.0.tgz /opt/queuesmanager/kafka_2.12-1.1.0.tgz 

RUN cd /opt/queuesmanager && \
	cp -R kafka_2.12-1.1.0.tgz/kafka_2.12-1.1.0 kafka_2.12-1.1.0 && \
	rm -R kafka_2.12-1.1.0.tgz && \
	ln -s kafka_2.12-1.1.0 kafka


RUN chown -R queuesmaster:queues /opt/queuesmanager/kafka
RUN chown -R queuesmaster:queues /opt/queuesmanager/kafka/

####################################################################################
#Add configurations and enviroment variables

ADD Default_Conf/server.properties /opt/queuesmanager/kafka/config/server.properties
RUN chown -R queuesmaster:queues /opt/queuesmanager/kafka/config/server.properties

RUN mkdir -p /var/log/kafka
RUN chown -R queuesmaster:queues /var/log/kafka

VOLUME /var/log/kafka

ENV KAFKA_HOME /opt/queuesmanager/kafka/

RUN echo export KAFKA_HOME=/opt/queuesmanager/kafka >> /opt/queuesmanager/.bashrc

ADD Default_Conf/AddkafkaHost /
RUN cat /AddkafkaHost >> /AddHosts
RUN rm /AddkafkaHost

HEALTHCHECK CMD curl -f http://localhost:9092/ || exit 1

EXPOSE 9092

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]

#BASED ON
# https://kafka.apache.org/ (official website)
# and my own knowledge