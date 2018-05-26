FROM ubuntu:16.04
MAINTAINER Ruben Garrido <ruben.garrido1@um.es>

USER root

# Update de system

RUN apt-get update
RUN apt-get install -y apt-utils && \
    apt-get -y upgrade
RUN apt-get -y install build-essential && \
	apt-get update && \
	apt-get -y upgrade
RUN apt-get -y install	libavahi-common-data \
			libssl-dev \
			curl \
			sudo \
			rsync \
			nano \
			ssh \
			pdsh \
			rsync \
			net-tools \
			python3 \
			wget \
			openjdk-8-jre \
			zip 


RUN mkdir -p /installedRegister/scala && \
	cd /installedRegister/scala && \
	wget https://www.scala-lang.org/files/archive/scala-2.12.6.deb && \
	dpkg -i scala-2.12.6.deb && \
	apt-get update && \
	apt-get -y install scala python3-pip

RUN apt-get update && \
    apt-get -y upgrade

####################################################################################
# Add users for hadoop and directories for hadoop AND GENERATE rsa_key

RUN mkdir /opt/bd && \
	groupadd -r hadoop  && \
	useradd -r -g hadoop -d /opt/bd -s /bin/bash hdmaster && \
	chown -R hdmaster:hadoop /opt/bd && \
	sudo su hdmaster && \
	mkdir ~/.ssh/ &&  \
	cd ~/.ssh/ \ &&  \
	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
	chmod 644 ~/.ssh/authorized_keys &&\
	cp -R ~/.ssh /opt/bd/.ssh && \
	chown -R hdmaster:hadoop /opt/bd/.ssh && \
	chown -R hdmaster:hadoop /opt/bd/.ssh && \
	chown -R root:root /root/.ssh/ 

# ssh configuration

# ssh config file (SET StrictHostKeyChecking “no”)
ADD Default_Conf/ssh_config /etc/ssh/ssh_config

# OPEN SSH PORT AND ADD ssh key

EXPOSE 22
####################################################################################

# Set envairoment variables

ENV JAVA_VERSION 8

#Java
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64 
ENV PDSH_RCMD_TYPE ssh

RUN cp /etc/skel/.bash_logout /opt/bd/ &&\
   	cp /etc/skel/.profile /opt/bd/ &&\
	cp /etc/skel/.bashrc /opt/bd/ &&\
	echo export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 >> /opt/bd/.bashrc &&\
	echo export PDSH_RCMD_TYPE=ssh >> /opt/bd/.bashrc &&\
	echo export PATH=$JAVA_HOME/bin:'$PATH' >> /opt/bd/.bashrc &&\
	chown -R hdmaster:hadoop /opt/bd/.bash_logout &&\
	chown -R hdmaster:hadoop /opt/bd/.profile &&\
	chown -R hdmaster:hadoop /opt/bd/.bashrc  &&\
	echo "ssh" > /etc/pdsh/rcmd_default

ADD  Default_Conf/AddHosts /

# IMPORTANT: if you don't use my yaml file, you have to change entrypoint.sh or /etc/hosts
# Add routes yml for hosts
# ADD  Default_Conf/AddHosts /

ADD Default_Conf/entrypoint.sh /
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
