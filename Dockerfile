FROM ubuntu:14.04

COPY . .

RUN mkdir -p /data/db

RUN mkdir -p /var/log/uwsgi

RUN touch /var/log/uwsgi/requests.log

RUN touch /var/log/uwsgi/errors.log

RUN apt-get update

RUN apt-get install -y build-essential

RUN apt-get install -y python2.7 python2.7-dev

RUN apt-get install -y curl

RUN apt-get install -y wget

RUN apt-get install -y git

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

RUN apt-get update

RUN apt-get install -y mongodb-org

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python2.7 get-pip.py

RUN pip install -r requirements.txt

RUN pip install uwsgi

RUN chmod +x ./start.sh

EXPOSE 80

CMD ./start.sh

