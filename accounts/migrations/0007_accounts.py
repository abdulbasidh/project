# Generated by Django 3.2.2 on 2021-05-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_registeredfroms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('salt', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
        ),
    ]