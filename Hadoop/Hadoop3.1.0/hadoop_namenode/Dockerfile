FROM karton91/hadoop_base310:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

HEALTHCHECK CMD curl -f http://localhost:50070/ || exit 1
EXPOSE 50070

# RUN sudo su hdmaster && hdfs namenode -format

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 50070

CMD ["/run.sh"]