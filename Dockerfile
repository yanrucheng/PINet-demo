FROM python:3.5-slim-stretch

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt
#RUN apt-get update
#RUN apt-get install -y libgtk2.0-dev

WORKDIR /app

COPY . .

CMD exec gunicorn --certfile cert.pem --keyfile key.pem \
	--bind :$PORT --workers 1 --threads 4 --timeout 0 app:app
