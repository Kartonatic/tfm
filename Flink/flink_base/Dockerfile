FROM karton91/hadoop_base310
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

RUN mkdir -p /opt/bd/streaming/ &&\
 chown -R hdmaster:hadoop /opt/bd/streaming && \
 apt-get install -y netcat

ADD flink-1.4.2-bin-hadoop28-scala_2.11.tgz /opt/bd/streaming/flink-1.4.2-bin-hadoop28-scala_2.11.tgz

RUN cd /opt/bd/streaming/ && \
	cp -R flink-1.4.2-bin-hadoop28-scala_2.11.tgz/flink-1.4.2 flink-1.4.2 && \
	rm -R flink-1.4.2-bin-hadoop28-scala_2.11.tgz && \
	ln -s flink-1.4.2 flink && \
	chown -R hdmaster:hadoop /opt/bd/streaming/flink && \ 
        chown -R hdmaster:hadoop /opt/bd/streaming/flink/

ADD Default_Conf/conf/ /opt/bd/streaming/flink/conf/
RUN chown -R hdmaster:hadoop /opt/bd/streaming/flink/conf/

ADD  Default_Conf/AddHostsFlink /

RUN cat /AddHostsFlink >> AddHosts && \
    echo export FLINK_HOME=/opt/bd/streaming/flink/  >> /opt/bd/.bashrc && \
    echo export LD_LIBRARY_PATH='$LD_LIBRARY_PATH':/opt/bd/hadoop/lib/native >> /opt/bd/.bashrc && \
    echo export PATH='$PATH':/opt/bd/streaming/flink/bin >> /opt/bd/.bashrc  && \
    mkdir -p /var/data/flink && \
    chown -R hdmaster:hadoop /var/data/flink/ &&\
    echo "ssh" > /etc/pdsh/rcmd_default 

VOLUME /var/data/flink


EXPOSE 6123 8081 42021


# Based on my own 