FROM karton91/mongodb_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

ADD run.sh /run.sh
ADD mongoUbicationServer.py /opt/bd/mongodb/mongoUbicationServer.py
RUN chmod a+x /run.sh /opt/bd/mongodb/mongoUbicationServer.py
RUN pip3 install pymongo
RUN pip3 install werkzeug

CMD ["/run.sh"]
