 FROM python:3.5-jessie
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 ADD requirements.txt /code/
 WORKDIR /code
 RUN pip install -r requirements.txt
 RUN apt-get update && apt-get install -y mysql-client