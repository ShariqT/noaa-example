service mongodb start

mongorestore --dbpath=/backupdb

uwsgi --ini /uwsgi.ini