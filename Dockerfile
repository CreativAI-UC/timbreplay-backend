FROM tiangolo/uvicorn-gunicorn-starlette:python3.7
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install --no-cache-dir -r /var/www/requirements.txt
#RUN git submodule update --remote

COPY . /app
