from django.urls import path

from .views import ObtainWeb3Token, Web3Message

app_name = 'web3auth'
urlpatterns = [
    path('', Web3Message.as_view(), name='index'),
    path('login',  ObtainWeb3Token.as_view(), name='login'),
    path('signup',  ObtainWeb3Token.as_view(), name='signup'),
]