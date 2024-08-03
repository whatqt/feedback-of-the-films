from django.urls import path
from .consumers import ChatSaport


ws_urlpatterns = [
    path('username=<username>', ChatSaport.as_asgi()),
]