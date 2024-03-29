import requests

from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework import permissions

from api.serializers.user_serializer import UserSerializer
from api.serializers.user_serializer import RegistrationSerializer

User = get_user_model()


class CreateAccount(APIView):
    """ Handles user account creation """
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


class UserAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
