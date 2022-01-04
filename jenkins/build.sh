#!/bin/bash

echo "build stage"
$MYSQL_ROOT_PASSWORD=khalid -p 3306:3306 
CREATE_SCHEMA=false
docker-compose up -d --build