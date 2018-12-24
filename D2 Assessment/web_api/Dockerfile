FROM python:3.6.4

MAINTAINER tester@anonymous.com

WORKDIR /var/www

COPY requirements.txt /var/www

RUN pip install -r requirements.txt

COPY . /var/www

CMD ["bash", "/var/www/server.sh"]
