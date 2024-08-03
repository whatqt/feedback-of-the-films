from django.urls import path
from .views import CreateChatSupport, ChatSupport

urlpatterns = [
    path('', CreateChatSupport),
    path('SupportChat/', ChatSupport)
]