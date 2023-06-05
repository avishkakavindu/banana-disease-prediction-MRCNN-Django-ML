import requests

from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework import permissions

from oauth2_provider.models import Application

from .serializers import UserSerializer

User = get_user_model()


class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                data = {
                    'client_id': settings.CLIENT_ID,
                    'client_secret': settings.CLIENT_SECRET,
                    'grant_type': 'password',
                    'username': request.data['username'],
                    'password': request.data['password']
                }

                # auto logs user to the system
                req = requests.post('http://127.0.0.1:8000/auth/token', data=data)

                context = req.json()
                return Response(context, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)
