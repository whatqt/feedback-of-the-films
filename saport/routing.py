from django.urls import path
from .consumers import ChatSaport


ws_urlpatterns = [
    path('', ChatSaport.as_asgi()),
]