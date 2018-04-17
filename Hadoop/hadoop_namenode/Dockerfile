FROM karton91/hadoop_base:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

HEALTHCHECK CMD curl -f http://localhost:50070/ || exit 1
EXPOSE 50070

RUN sudo su hdmaster && hdfs namenode -format
# hdfs --daemon start namenode

CMD ["/etc/bootstrap.sh", "-bash"]
