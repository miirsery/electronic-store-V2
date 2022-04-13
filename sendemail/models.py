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
    users = models.ManyToManyField(User)
    is_send = models.CharField(choices=send, max_length=255)

    class Meta:
        verbose_name = 'Писмо'
        verbose_name_plural = 'Письма'
        
def email_post_save(sender, instance, created,  *args, **kwargs):
    if created:
        print("feffefefgregrgeergergegegegrgergegereregegegegegf")
        if instance.is_send == 'SEND':
            user_list = []
            print(MailingLetters.objects.get(id=instance.id).users.all())
            print(instance.users.all())
            for user in instance.users.all():
                user_list.append(user.email)
            send_mail(str(instance.subject), str(instance.message), settings.EMAIL_HOST_USER, user_list)
            print(instance.is_send)
            print(user_list)


post_save.connect(email_post_save, sender=MailingLetters)


