from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, PersonsSerializer, FormSerializer, AccountsSerializer, DecrypSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from accounts.models import RegisteredFroms, Accounts, Decryp
import bcrypt
from Crypto.Cipher import DES3



# Register API
class PersonsAPI(generics.GenericAPIView):
    serializer_class = PersonsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        persons = serializer.save(using='ext')
        ##
        refresh = RefreshToken.for_user(persons)
        return Response({
            "Persons": PersonSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })

# FormRegister API
class FormRegisterApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        form = RegisteredFroms.objects.filter(username = request.user.id)
        serializer = FormSerializer(form, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        username = request.data.get('username')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        if RegisteredFroms.objects.filter(username=username).exists():
            data = {
                'username already exists'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif RegisteredFroms.objects.filter(email=email).exists():
            data = {
                'email already exists'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        elif RegisteredFroms.objects.filter(phone_number=phone_number).exists():
            data = {
                'phone_number already exists'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {
                'username': request.data.get('username'),
                'email': request.data.get('email'),
                'phone_number': request.data.get('phone_number'),
                'password': request.data.get('password'),
            }
            serializer = FormSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class DecrypApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        decryp = Decryp.objects.filter(username = request.user.id)
        serializer = DecrypSerializer(decryp, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'salt': request.data.get('salt'),
        }
        serializer = DecrypSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PersonAPI(generics.GenericAPIView):
    serializer_class = FormSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ##
        refresh = RefreshToken.for_user(RegisteredFroms)
        return Response({
            "Persons": FormSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })


class LoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if RegisteredFroms.objects.filter(username=username).exists():
            if RegisteredFroms.objects.filter(password=password).exists():
                refresh = RefreshToken.for_user(RegisteredFroms)
                return Response ({
                    "username": username,
                    "password": password,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                })
            else:
                return Response ({
                    "Password does not match"
                })
        else:
            return Response ({
                "Username does not match"
            })


class AccountsApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        accounts = Accounts.objects.filter(username = request.user.id)
        serializer = AccountsSerializer(accounts, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
        }
        username = request.data.get('username')
        password = request.data.get('password')
        pepper = "184fc7ef21aab40368d0401f85041b6224eb4c09f02f8c7a9627b7bf1d893777"
        peppass=pepper+password
        salt = bcrypt.gensalt()
        newpass = peppass.encode("utf-8")
        newpassall = bcrypt.hashpw(newpass, salt)

        p = Accounts(username=username, password=newpassall, salt=salt)
        p.save()
        return Response({
            "username": username,
            "password": newpass,
            "salt": salt,
            "newpassall": newpassall
        })
