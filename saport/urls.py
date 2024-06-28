from django.urls import path
from .views import ChatSaport

urlpatterns = [
    path('<str:name_saport_room>', ChatSaport)
]