#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

# run Celery worker for our project NewsReaderDjango with Celery configuration stored in Celeryconf
su -m myuser -c "rm /tmp/celerybeat-doshi.pid > /dev/null"
su -m myuser -c "celery beat -A NewsReaderDjango.celery -l info --pidfile=/tmp/celerybeat-doshi.pid"