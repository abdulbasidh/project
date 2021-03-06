# Generated by Django 3.2.2 on 2021-05-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_phn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Persons',
                'managed': False,
            },
        ),
    ]
