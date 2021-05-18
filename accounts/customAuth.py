from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from accounts.models import Persons

class PersonsBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        try:
            persons = Persons.objects.get(email=email)
            if persons.persons.check_password(password) is True:
                return persons.persons
        except Persons.DoesNotExist:
            pass
