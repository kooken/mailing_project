# Generated by Django 5.0.6 on 2024-07-07 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_alter_client_owner_alter_mailing_mailing_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='mailing_owner',
        ),
    ]
