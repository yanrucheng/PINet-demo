FROM python:3.5-slim-stretch

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY . .

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 0 app:app
