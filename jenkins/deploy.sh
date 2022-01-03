#!/bin/bash

echo "deploy stage"

ssh jenkins@swarm-manager docker stack deploy --compose-file docker-compose.yaml bootcamp-project