FROM karton91/hadoop_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

ADD zookeeper-3.4.10.tar.gz /opt/zookeeper-3.4.10.tar.gz

RUN cd /opt && ls 

RUN cd /opt && \
	cp -R zookeeper-3.4.10.tar.gz/zookeeper-3.4.10 zookeeper-3.4.10 && \
	rm -R zookeeper-3.4.10.tar.gz && \
	ln -s zookeeper-3.4.10 zookeeper

RUN chown -R hdmaster:hadoop /opt/zookeeper
RUN chown -R hdmaster:hadoop /opt/zookeeper/

ADD Default_Conf/zoo.cfg /opt/zookeeper/conf/zoo.cfg
ADD Default_Conf/zoo_replicated.cfg.dynamic /opt/zookeeper/conf/zoo_replicated.cfg.dynamic

RUN chown -R hdmaster:hadoop /opt/zookeeper/conf/

RUN mkdir -p /var/data/zookeeper
RUN mkdir -p /var/log/zookeeper

RUN chown -R hdmaster:hadoop /var/log/zookeeper
RUN chown -R hdmaster:hadoop /var/data/zookeeper

ENV ZOOKEEPER_HOME /opt/zookeeper/
ENV ZOOBINDIR /opt/zookeeper/bin
ENV ZOOCFGDIR /opt/zookeeper/conf

RUN echo export ZOOKEEPER_HOME=/opt/zookeeper >> /opt/bd/.bashrc
RUN echo export ZOOBINDIR=/opt/zookeeper/bin >> /opt/bd/.bashrc
RUN echo export ZOOCFGDIR=/opt/zookeeper/conf >> /opt/bd/.bashrc
RUN echo export PATH='$PATH':$ZOOKEEPER_HOME/bin >> /opt/bd/.bashrc

VOLUME /var/log/zookeeper
VOLUME /var/data/zookeeper

ADD Default_Conf/AddZooKeeperHost /

HEALTHCHECK CMD curl -f http://localhost:2181/ || exit 1

EXPOSE 2181 2888 3888

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]


#BASED ON https://github.com/31z4/zookeeper-docker