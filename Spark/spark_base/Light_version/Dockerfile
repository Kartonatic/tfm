FROM karton91/hadoop_base310
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

RUN mkdir -p /opt/bd/streaming/ && chown -R hdmaster:hadoop /opt/bd/streaming

ADD spark-2.3.0-bin-hadoop2.7.tgz /opt/bd/streaming/spark-2.3.0-bin-hadoop2.7.tgz

RUN cd /opt/bd/streaming/ && \
	cp -R spark-2.3.0-bin-hadoop2.7.tgz/spark-2.3.0-bin-hadoop2.7 spark-2.3.0-bin-hadoop2.7 && \
	rm -R spark-2.3.0-bin-hadoop2.7.tgz && \
	ln -s spark-2.3.0-bin-hadoop2.7 spark && \
	chown -R hdmaster:hadoop /opt/bd/streaming/spark && \ 
        chown -R hdmaster:hadoop /opt/bd/streaming/spark/

RUN cd /opt/bd/streaming/spark/jars && \
	wget central.maven.org/maven2/org/elasticsearch/elasticsearch-hadoop/6.2.4/elasticsearch-hadoop-6.2.4.jar &&\
	chown -R hdmaster:hadoop /opt/bd/streaming/spark/jars/elasticsearch-hadoop-6.2.4.jar

ADD Default_Conf/conf/ /opt/bd/streaming/spark/conf/
RUN chown -R hdmaster:hadoop /opt/bd/streaming/spark/conf/


# ADD  Default_Conf/AddHostsSpark /
# RUN cat /AddHostsSpark >> AddHosts 
ADD run.sh /run.sh

RUN echo export SPARK_HOME=/opt/bd/streaming/spark/  >> /opt/bd/.bashrc && \
    echo export LD_LIBRARY_PATH='$LD_LIBRARY_PATH':/opt/bd/hadoop/lib/native >> /opt/bd/.bashrc && \
    echo export PYSPARK_PYTHON=python3 >> /opt/bd/.bashrc  && \
    echo export PATH='$PATH':/opt/bd/streaming/spark/bin >> /opt/bd/.bashrc  && \
    echo export PYTHONIOENCODING=utf8 >> /opt/bd/.bashrc  && \
    chmod a+x /run.sh && \
    mkdir -p /var/data/spark && \
    chown -R hdmaster:hadoop /var/data/spark/

VOLUME /var/data/spark


EXPOSE 8080 7077 6066 18080 44247 9999

ADD activeSpark.sh /activeSpark.sh
RUN chmod a+x /activeSpark.sh

CMD ["/run.sh"]

# Based on https://linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/