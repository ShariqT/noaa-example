service mongod start

mongorestore --archive=/noaadb.archive

uwsgi --ini /uwsgi.ini