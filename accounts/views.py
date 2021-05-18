from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, PersonsSerializer
from rest_framework_simplejwt.tokens import RefreshToken


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
