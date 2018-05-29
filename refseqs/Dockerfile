# nginx-gunicorn-flask

FROM python:2.7-alpine

RUN apk update && \
	apk add python postgresql-client postgresql-dev gcc musl-dev

# Setup flask application
RUN mkdir -p /deploy/app
COPY app/requirements.txt /deploy/app/requirements.txt
RUN pip install -r /deploy/app/requirements.txt gunicorn
COPY app /deploy/app

EXPOSE 5000
WORKDIR "/deploy/app"
# Start processes
ENTRYPOINT ["/usr/local/bin/gunicorn"]
CMD ["hello:app", "-b", "0.0.0.0:5000"]
