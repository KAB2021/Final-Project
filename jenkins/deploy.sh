#!/bin/bash

echo "deploy stage"
scp docker-compose.yml jenkins@swarm-manager:/home/jenkins/docker-compose.yml
checkout scm docker.image('mysql:5.7').withRun('-e "MYSQL_ROOT_PASSWORD= khalid" -p 3306:3306')
ssh jenkins@swarm-manager \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    docker stack deploy --compose-file docker-compose.yml bootcamp-project \
    