
#!/bin/bash
chown -R hdmaster:hadoop /var/history/hadoop
sudo -u hdmaster -g hadoop $HADOOP_HOME/bin/yarn historyserver