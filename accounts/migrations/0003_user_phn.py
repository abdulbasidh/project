# Generated by Django 3.2.2 on 2021-05-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_phnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phn',
            field=models.CharField(default=1234567890, max_length=10),
            preserve_default=False,
        ),
    ]