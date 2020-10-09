#!/bin/bash
app="timbreplay.starlette"
env="dev"
sourceVersion="8"
targetVersion="1"
docker tag ${app}.${env}:${sourceVersion} gcr.io/timbreplay/${app}.${env}:${targetVersion}
docker push gcr.io/timbreplay/${app}.${env}:${targetVersion}
