service mongodb start

mongorestore --archive=/testapi/noaa.archive

uwsgi --ini /uwsgi.ini