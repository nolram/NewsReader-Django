#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

# run Celery worker for our project NewsReaderDjango with Celery configuration stored in Celeryconf
su -m myuser -c "celery worker -A NewsReaderDjango.celery -l info"