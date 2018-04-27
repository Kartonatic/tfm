FROM karton91/kafka_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

HEALTHCHECK CMD curl -f http://localhost:9092/ || exit 1

EXPOSE 9092

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
