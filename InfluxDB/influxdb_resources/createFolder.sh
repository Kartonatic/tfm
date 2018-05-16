rm -r influxdb_base
rm -r influxdb
rm -r chronograf
rm -r kapacitor
rm -r telegraf

mkdir -p influxdb_base
mkdir -p influxdb_base/data influxdb_base/log influxdb_base/lib

mkdir -p influxdb
mkdir -p influxdb/data influxdb/log influxdb/lib

mkdir -p chronograf
mkdir -p chronograf/data chronograf/log chronograf/lib

mkdir -p kapacitor
mkdir -p kapacitor/data kapacitor/log kapacitor/lib

mkdir -p telegraf
mkdir -p telegraf/data telegraf/log telegraf/lib
