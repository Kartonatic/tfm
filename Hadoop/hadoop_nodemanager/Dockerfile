FROM karton91/hadoop_base:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

HEALTHCHECK CMD curl -f http://localhost:8042/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8042

CMD ["/run.sh"]