# Generated by Django 4.0.4 on 2022-04-29 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketcontrol', '0008_alter_ticket_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Permission',
        ),
    ]
