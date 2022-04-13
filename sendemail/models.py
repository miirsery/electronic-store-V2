from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from user.models import User


class MailingLetters(models.Model):

    send = (
        ('SEND', 'Отправить'),
        ('Draft', 'Черновик'),
    )

    subject = models.CharField(max_length=75)
    message = models.TextField(max_length=1024)
    attachments = models.FileField()
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    is_send = models.CharField(choices=send, max_length=255)

    class Meta:
        verbose_name = 'Писмо'
        verbose_name_plural = 'Письма'



