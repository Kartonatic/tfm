FROM karton91/hadoop_base276:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root


HEALTHCHECK CMD curl -f http://localhost:50075/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 50075

CMD ["/run.sh"]