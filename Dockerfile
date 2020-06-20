FROM tiangolo/uvicorn-gunicorn-starlette:python3.7
ENV MIDI_PATH /var/www/app/midi
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

COPY ./app /app