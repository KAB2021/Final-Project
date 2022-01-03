#!/bin/bash

echo "deploy stage"

ssh jenkins@khalid-jenkins docker stack deploy --compose-file docker-compose.yaml bootcamp-project