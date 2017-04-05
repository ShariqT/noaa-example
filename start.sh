service mongodb start

mongorestore /backupdb/admin/system.users.bson

mongorestore /backupdb/oceans/ocean_data.bson

mongorestore /backupdb/oceans/stations.bson

uwsgi --ini /uwsgi.ini