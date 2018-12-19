#!/bin/bash

# use manage.py inside the running container from the host's shell

# enter the django shell
# ./docker/django/manage.sh shell

# work with migrations
# ./docker/django/manage.sh makemigrations
# ./docker/django/manage.sh migrate

ARGS="$@"
if [[ -z $ARGS ]]
then
    ARGS="help"
fi

docker-compose exec django python /code/manage.py $ARGS