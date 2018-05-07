FROM karton91/spark_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

ADD run.sh /run.sh

ADD activeSpark.sh /activeSpark.sh
RUN chmod a+x /activeSpark.sh

CMD ["/run.sh"]