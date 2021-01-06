import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

local_broker = 'amqp://my-rabbit:5672'
app = Celery('myshop', broker=local_broker)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
