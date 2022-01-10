# core/tasks.py
import time
from celery import shared_task

from django.core.mail import send_mail

# @shared_task
# def add(x, y):
#     return x + y

@shared_task
def send_email_task(email, content):

    subject = 'Hello from Celery'
    # message = 'This is a test email sent asynchronously with Celery'
    message = content
    time.sleep(5)
    return send_mail(
        subject,
        message,
        'liangzhang0731@gmail.com',
        [email],
        fail_silently=False,
    )