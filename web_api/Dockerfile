FROM python:3.6.4

MAINTAINER tester@anonymous.com
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 \
  && apt-get -q update \
  && echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main" | tee /etc/apt/sources.list.d/mongodb-org-3.6.list \
  && apt-get -q update \
  && apt-get install -y mongodb-org

WORKDIR /var/www

COPY requirements.txt /var/www

RUN pip install -r requirements.txt

COPY . /var/www

CMD ["bash", "/var/www/server.sh"]
