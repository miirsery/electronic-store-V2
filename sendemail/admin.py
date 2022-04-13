from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail

from sendemail.models import MailingLetters


@admin.register(MailingLetters)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_send')
    search_fields = ('subject',)
    list_filter = ('is_send',)

    


