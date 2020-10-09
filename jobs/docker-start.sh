#!/bin/bash
app="timbreplay.starlette"
env="dev"
version="9"
docker build -t ${app}.${env}:${version} .
docker run -d -p 80:80 --name=${app}.${env}.v${version} ${app}.${env}:${version}
