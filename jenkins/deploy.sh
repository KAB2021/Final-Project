#!/bin/bash

echo "deploy stage"
scp docker-compose.yml jenkins@swarm-manager:/home/jenkins/docker-compose.yml
ssh jenkins@swarm-manager \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    docker stack deploy --compose-file docker-compose.yml bootcamp-project