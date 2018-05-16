FROM karton91/influxdb_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

VOLUME /var/data/influxdb /var/log/influxdb /var/lib/influxdb

# EXPOSE 8086 8082 8089 8086 9092

EXPOSE 8086 8082 8089 8086 9092

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]