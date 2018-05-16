#!/bin/bash
chmod a+rw -R /var/data/elastic/
chmod a+rw -R /var/log/elastic/

sudo -u elastic -g bbdd /opt/bd/elastic/elasticsearch/bin/elasticsearch

echo "¡ERROR ELASTICSEARCH!USA: 'sudo sysctl -w vm.max_map_count=262144' en tu maquina"


