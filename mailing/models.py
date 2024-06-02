from django.db import models

# Create your models here.
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}

MAILING_PERIODICITY = (
    ('one time', 'once'),
    ('day', 'daily'),
    ('week', 'weekly'),
    ('month', 'monthly'),
)

MAILING_STATUS = (
    ('created', 'mailing_created'),
    ('started', 'mailing_started'),
    ('completed', 'mailing_complete'),
)

ATTEMPT_STATUS = (
    ('successful', 'attempt_successful'),
    ('failed', 'attempt_failed'),
)

class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='email')
    first_name = models.CharField(max_length=100, **NULLABLE, verbose_name='client_name')
    last_name = models.CharField(max_length=100, **NULLABLE,  verbose_name='client_surname')
    comment = models.TextField(**NULLABLE, verbose_name='comment')
    owner = models.ForeignKey(User, default=False, on_delete=models.CASCADE, verbose_name='owner')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='message_subject')
    text = models.TextField(**NULLABLE, verbose_name='message_text')
    owner = models.ForeignKey(User, default=False, on_delete=models.CASCADE, verbose_name='message_user')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

class Mailing (models.Model):
    mailing_sent = models.DateTimeField(verbose_name='send_timestamp')
    mailing_end = models.DateTimeField(verbose_name='end_timestamp')
    mailing_periodicity = models.CharField(max_length=100, choices=MAILING_PERIODICITY, verbose_name='periodicity')
    mailing_status = models.CharField(max_length=100, choices=MAILING_STATUS, verbose_name='status')
    mailing_clients = models.ManyToManyField(Client, verbose_name='clients')
    mailing_message = models.ForeignKey(Message, on_delete=models.CASCADE, **NULLABLE, verbose_name='message')
    mailing_owner = models.ForeignKey(User, default=False, on_delete=models.CASCADE, verbose_name='mailing_user')

    def __str__(self):
        return f'{self.mailing_sent}'

    class Meta:
        verbose_name = 'mailing'
        verbose_name_plural = 'mailings'

class Attempt (models.Model):
    time_attempt = models.DateTimeField(auto_now_add=True, verbose_name='attempt_time')
    attempt_status = models.CharField(max_length=100, choices=ATTEMPT_STATUS, verbose_name='attempt_status')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='mailing')
    server_response = models.TextField(**NULLABLE, verbose_name='server_response')

    def __str__(self):
        return f'{self.time_attempt} {self.attempt_status}'

    class Meta:
        verbose_name = 'attempt'
        verbose_name_plural = 'attempts'