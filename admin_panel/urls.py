from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_admin),
    path('views_open_ticket', views.views_open_ticket)
]