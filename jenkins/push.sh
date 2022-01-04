#!/bin/bash

echo "push stage"
MYSQL_ROOT_PASSWORD=khalid CREATE_SCHEMA=false
docker-compose push