#!/bin/bash

echo "build stage"
$MYSQL_ROOT_PASSWORD=khalid CREATE_SCHEMA=false
docker-compose up -d --build