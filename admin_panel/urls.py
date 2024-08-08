from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_admin),
    path('views_open_ticket', views.views_open_ticket),
    path('closed_ticket_db', views.closed_ticket_db)
]