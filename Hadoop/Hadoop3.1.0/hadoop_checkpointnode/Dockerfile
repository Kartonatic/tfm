FROM karton91/hadoop_base310:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root


HEALTHCHECK CMD curl -f http://localhost:50090/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 50090

CMD ["/run.sh"]