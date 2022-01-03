#!/bin/bash

echo "deploy stage"
scp docker-compose.yml jenkins@swarm-manager:/home/jenkins/docker-compose.yml
ssh jenkins@swarm-manager docker stack deploy --compose-file docker-compose.yml bootcamp-project