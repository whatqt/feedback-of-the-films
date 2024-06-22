from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_reg),
    path('log_in', views.log_in),
    path('log_out', views.log_out),
    path('films',views.films),
    path('reg', views.register),
]