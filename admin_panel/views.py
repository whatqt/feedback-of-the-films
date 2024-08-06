from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from support.models import DataTicket


def index_admin(request: HttpRequest):
    username = request.user.username
    check_staff = User.objects.filter(username=username).values()[0]
    if check_staff['is_staff'] is True:
        return HttpResponse("Добро пожаловать в панель администратора")

def views_open_ticket(request: HttpRequest):
    check_staff = User.objects.filter(username=request.user.username).values()[0]
    if check_staff['is_staff'] is True:
        data_ticket = DataTicket.objects.values_list('username_create_ticket','id_ticket', 'accept_staff_name')
        print(data_ticket)
        return render(request, 'views_open_ticket.html', context={'data_ticket': data_ticket})