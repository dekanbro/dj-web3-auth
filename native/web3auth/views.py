from django.conf import settings
from django.contrib.auth import login, logout

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from datetime import datetime

from .serializers import Web3TokenSerializer, SignupSerializer
from .authentication import Web3Backend

from native.users.models import User

class Web3Message(APIView):
    permission_classes = (AllowAny, )
    # authentication_classes = (Web3Backend, )

    def get(self, request, *args, **kwargs):
        return Response(
                status=200, 
                data={
                    'web3message': settings.WEB3_MESSAGE,}) 


class ObtainWeb3Token(APIView):

    permission_classes = (AllowAny, )
    # authentication_classes = (Web3Backend, )
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            signature = serializer.data['signature']
            username = serializer.data['username']
            email = serializer.data['email']
            # if user does not exist create it
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create(
                    username=username, email=email)

            token, create = Token.objects.get_or_create(user=user)

            # check that signature matches token phrase and return user with that eth account
            signed_user = Web3Backend.authenticate(
                self, request, token=settings.WEB3_MESSAGE, signature=signature)
            # if uesr eth account (username) matches signature user return token for auth
            if(signed_user == user):
                login(request, user)
                return Response(status=200, data={'status': 'successfull login have a tokem :)', 
                    'token': str(token), 'addr': user.username, 'email': user.email})
            else:
                logout(request)
                return Response({'error': 'Nope'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Nope'}, status=status.HTTP_400_BAD_REQUEST)

