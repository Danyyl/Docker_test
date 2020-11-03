import logging

from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

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