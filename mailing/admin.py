from django.contrib import admin
from mailing.models import Client, Mailing, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Mailing)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('mailing_message', 'mailing_periodicity', 'mailing_status')


@admin.register(Message)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('subject',)
