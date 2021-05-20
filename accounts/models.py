from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, UserManager


class RegisteredFroms(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone_number = models.CharField(max_length=60)
    password = models.CharField(max_length=60)


class User(models.Model):
    username = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class PersonsManager(BaseUserManager):
    def create_persons(self, email, username, phone, password=None):
        if not email:
            raise ValueError('User shoul have email')

        email = self.normalize_email(email)
        persons = self.model(email=email, username=username, phone=phone)

        persons.set_password(password)
        persons.save(using='ext')

class Persons(AbstractBaseUser):
    id = models.IntegerField(blank=False)
    username = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    objects = PersonsManager()


    class Meta:
        managed = False
        db_table = 'Persons'
