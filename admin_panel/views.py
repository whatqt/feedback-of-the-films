from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from support.models import DataTicket, DataClosedTicket
from datetime import datetime




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

def closed_ticket_db(request: HttpRequest):
    if request.user.is_staff is True:
        if request.method == 'POST':
            id_ticket = request.POST.get('id_ticket')
            print(id_ticket)
            info_ticket = DataTicket.objects.filter(id_ticket=id_ticket).values_list()[0]
            print(info_ticket)
            print(info_ticket[2])
            print(info_ticket[4])

            DataClosedTicket.objects.create(
                id_ticket=info_ticket[0], username_create_ticket=info_ticket[1],
                date_create_ticket=info_ticket[2], accept_staff_name=info_ticket[3],
                date_accept_ticket=info_ticket[4], date_closed_ticket=datetime.today()
            )
            DataTicket.objects.filter(id_ticket=id_ticket).delete()
            print(info_ticket)
            return HttpResponse('Тикет закрыт')

