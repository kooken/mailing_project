from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Mailing, Attempt


def send_mailing():
    now = datetime.now()
    mailings = Mailing.objects.filter(mailing_sent__lte=now)

    for mailing in mailings:
        clients = mailing.mailing_clients.all()
        message = mailing.mailing_message
        for client in clients:
            try:
                send_mail(
                    subject=message.subject,
                    message=message.text,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                )
                Attempt.objects.create(time_attempt=datetime.now(),
                                       attempt_status="OK",
                                       mailing=mailing)
            except Exception as e:
                Attempt.objects.create(time_attempt=datetime.now(),
                                       attempt_status="Error",
                                       mailing=mailing,
                                       server_response=e)

        if mailing.mailing_periodicity == 'daily':
            mailing.mailing_sent += timedelta(days=1)
        elif mailing.mailing_periodicity == 'weekly':
            mailing.mailing_sent += timedelta(weeks=1)
        elif mailing.mailing_periodicity == 'monthly':
            mailing.mailing_sent += timedelta(days=30)
        mailing.save()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=60)

    if not scheduler.running:
        scheduler.start()
