`curl 'http://0.0.0.0:56734/generate' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en,es-CL;q=0.8,es;q=0.5,en-US;q=0.3' --compressed -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -s -o /dev/null -w  "%{time_starttransfer}\n"`

`gcloud auth login`
`gcloud config set project timbreplay`

`docker push gcr.io/timbreplay/timbreplay.starlette`

## Submodules