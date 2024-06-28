from django.urls import path
from .consumers import ChatSaport


ws_urlpatterns = [
    path('<str:name_saport_room>', ChatSaport.as_asgi()),
]