#!/bin/bash

# use pip inside the running container from the host's shell

# interact with pip
# ./docker/django/pip.sh install -r requirements.txt --upgrade

# output the requirements.txt
# ./docker/django/pip.sh freeze | dos2unix > requirements.txt

ARGS="$@"
if [[ -z $ARGS ]]
then
    ARGS="help"
fi

docker-compose exec django pip $ARGS