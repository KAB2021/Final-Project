#!/bin/bash

echo "build stage"
export MYSQL_ROOT_PASSWORD=khalid CREATE_SCHEMA=false
docker-compose -d --build