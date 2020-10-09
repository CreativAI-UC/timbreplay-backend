# Commands

`curl 'http://127.0.0.1:8000/generate' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en,es-CL;q=0.8,es;q=0.5,en-US;q=0.3' --compressed -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Accept-Encoding: gzip'    -s -o /dev/null -w  "%{time_starttransfer}\n"`

`source /Users/mandrade/Projects/python-envs/timbreplay/bin/activate`

`curltime 127.0.0.1/generate\?x=20\&y=20`

## Goocle cloud platform


`gcloud auth login`- login on console

`gcloud config set project timbreplay`- ensure the correct project is set

`docker push gcr.io/timbreplay/timbreplay.starlette`- upload your image

## Submodules

`git submodule add https://github.com/CreativAI-UC/TimbreNet.git`

`git submodule update --remote`

`source /Users/mandrade/Projects/tensorflow-env/bin/activate`

## Docker

`docker ps` - Show all docker processes, add `-a` to see all

`docker container ls`- show docker containers

`docker image ls`- show docker images

## file formats

batch conversion of files `find . -iname \*.wav -type f -exec ffmpeg -i {} -codec:a libmp3lame -qscale:a 2 {}.mp3 -y \;`