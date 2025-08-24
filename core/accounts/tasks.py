from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_password_reset_email_task(recipient_email, reset_url):
    subject = 'Password Reset Request'
    message = f'Click the link to reset your password: {reset_url}'
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )