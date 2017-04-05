FROM ubuntu:14.04

COPY . .

RUN mkdir -p /data/db

RUN mkdir -p /var/log/uwsgi

touch /var/log/uwsgi/requests.log

touch /var/log/uwsgi/errors.log

RUN apt-get update

RUN apt-get install -y build-essential

RUN apt-get install -y python2.7 python2.7-dev

RUN apt-get install -y curl

RUN apt-get install -y wget

RUN apt-get install -y git

RUN apt-get install -y nano

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb.list

RUN apt-get update

RUN apt-get install -y mongodb

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python2.7 get-pip.py

RUN pip install -r requirements.txt

RUN pip install uwsgi

RUN chmod +x ./start.sh

EXPOSE 80

CMD ./start.sh

