from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail

from sendemail.models import MailingLetters


@admin.register(MailingLetters)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_send')
    search_fields = ('subject',)
    list_filter = ('is_send',)

    def save_model(self, request, obj, form, change):
        obj.save()
        print(obj.users)
        if obj.is_send == 'SEND':
            # user_list = []
            # print(obj.users.all())
            # for user in obj.users.all():
            #     user_list.append(user.email)

            send_mail(str(obj.subject), str(obj.message), settings.EMAIL_HOST_USER, [obj.users.email])
            print(obj.is_send)
            # print(user_list)


