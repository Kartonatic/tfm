FROM karton91/hadoop_base276:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

HEALTHCHECK CMD curl -f http://localhost:8188/ || exit 1

HEALTHCHECK CMD curl -f http://localhost:19888/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8188 19888

CMD ["/run.sh"]