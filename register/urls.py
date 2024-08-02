from django.urls import path
from . import views



urlpatterns = [
    path('', views.register),
    path('log_in', views.log_in),
    path('log_out', views.log_out),
    path('films',views.films),
]