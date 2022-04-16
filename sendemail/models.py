from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User


class MailingLetters(models.Model):

    send = (
        ('SEND', 'Отправить'),
        ('Draft', 'Черновик'),
    )

    subject = models.CharField(max_length=75)
    message = models.TextField(max_length=1024)
    attachments = models.FileField()
    users = models.ManyToManyField(User)
    is_send = models.CharField(choices=send, max_length=255)


    class Meta:
        verbose_name = 'Писмо'
        verbose_name_plural = 'Письма'






