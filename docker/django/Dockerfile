 FROM python:3.5-jessie
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 RUN apt-get update && apt-get install -y mysql-client
 ADD . /code/
