# Generated by Django 3.2.2 on 2021-05-17 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_phn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phn',
        ),
    ]
