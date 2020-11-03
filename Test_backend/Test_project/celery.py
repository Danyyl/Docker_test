import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'Test_project.settings')

app = Celery('Test_project')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()