
#!/bin/bash
chown -R hdmaster:hadoop /var/log/hadoop/
chmod a+rw -R /var/log/hadoop/
sudo -u hdmaster -g hadoop $HADOOP_HOME/bin/mapred historyserver
# echo "Se ha lanzado el history del mapred"
# sudo -u hdmaster -g hadoop $HADOOP_HOME/bin/yarn historyserver