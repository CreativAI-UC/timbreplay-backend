#!/bin/bash
app="timbreplay.starlette"
version="1"
docker build -t ${app}:${version} .
docker run -d -p 56734:80 --name=${app} ${app}:${version}
