FROM karton91/mongodb_base
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root
RUN apt-get -y install python python-pip python-dev build-essential 
RUN pip install pymongo
ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
