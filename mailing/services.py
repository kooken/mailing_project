from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing


def send_mailing():
    now = datetime.now()
    mailings = Mailing.objects.filter(next_send_time__lte=now)

    for mailing in mailings:
        clients = mailing.client.all()
        for client in clients:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
            )

        if mailing.regularity == 'daily':
            mailing.next_send_time += timedelta(days=1)
        elif mailing.regularity == 'weekly':
            mailing.next_send_time += timedelta(weeks=1)
        elif mailing.regularity == 'monthly':
            mailing.next_send_time += timedelta(days=30)
        mailing.save()


def start_scheduler():
    print('Starting scheduler...')
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=60)

    if not scheduler.running:
        scheduler.start()

    print('Scheduler started')