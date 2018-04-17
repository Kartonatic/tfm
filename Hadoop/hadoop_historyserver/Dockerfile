FROM karton91/hadoop_base:latest
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

HEALTHCHECK CMD curl -f http://localhost:8188/ || exit 1

ENV YARN_CONF_yarn_timeline___service_leveldb___timeline___store_path=/var/history/hadoop/yarn/timeline
RUN mkdir -p /var/history/hadoop/yarn/timeline
RUN chown -R hdmaster:hadoop /var/history/hadoop
VOLUME /var/history/hadoop/yarn/timeline

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8188

CMD ["/run.sh"]