from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand
from mailing.models import Mailing, Message


class Command(BaseCommand):

    def handle(self, *args, **options):
        mailing = Mailing.objects.filter(mailing_message=Message.text)

        send_mail(
            subject=Message.subject,
            message=Message.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.mailing_clients.all()]
        )
