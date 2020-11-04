import logging

from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings


from my_test.models import Employees
import Test_project.celery as celery_settings


@celery_settings.app.task(bind=True, default_retry_delay=2)
def my_send_mail(self, email, token):
    try:
        logging.warning("yes? i do it")
        send_mail('tokens', token, 'danyyl_l@ukr.net', [email], fail_silently=False, auth_user='danyyl_l@ukr.net',
                  auth_password='kj,tyrj9',
                  connection=None, html_message=None)
    except Exception as e:
        logging.error(str(e))
        self.retry(exc=e, max_retries=3)


@celery_settings.app.task(bind=True)
def test_task(self):
    logging.warning("Hello? i am work")
    try:
        users = Employees.objects.all()
        logging.warning(str(users))
        for temp_user in users:
            try:
                logging.warning("send mail")
                send_mail('tokens', "Hello, user", 'danyyl_l@ukr.net', [temp_user.email], fail_silently=False, auth_user='danyyl_l@ukr.net',
                        auth_password='kj,tyrj9', connection=None, html_message=None)
            except Exception as e:
                logging.warning(str(e))
    except Exception as e:
        logging.warning(str(e))


celery_settings.app.conf.beat_schedule = {
   'my_spam': {
       "task": "my_test.tasks.test_task",
       "schedule": 3.0
   }
}