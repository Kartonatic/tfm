FROM karton91/zookeeper_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

ADD kafka_2.12-1.1.0.tgz /opt/kafka_2.12-1.1.0.tgz

RUN cd /opt && ls 

RUN cd /opt && \
	cp -R kafka_2.12-1.1.0.tgz/kafka_2.12-1.1.0 kafka_2.12-1.1.0 && \
	rm -R kafka_2.12-1.1.0.tgz && \
	ln -s kafka_2.12-1.1.0 kafka


ADD Default_Conf/server.properties /opt/kafka/config/server.properties

RUN mkdir -p /var/log/kafka

RUN chown -R hdmaster:hadoop /opt/kafka
RUN chown -R hdmaster:hadoop /opt/kafka/
RUN chown -R hdmaster:hadoop /var/log/kafka

VOLUME /var/log/kafka

ENV KAFKA_HOME /opt/kafka/

RUN echo export KAFKA_HOME=/opt/kafka >> /opt/bd/.bashrc

ADD Default_Conf/AddkafkaHost /

HEALTHCHECK CMD curl -f http://localhost:9092/ || exit 1

EXPOSE 9092

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
