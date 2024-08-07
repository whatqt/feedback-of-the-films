from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db import connection
from django.db.utils import IntegrityError, ProgrammingError
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import random_id_ticket
from .models import DataTicket
from .cache_id_ticket import cache_id_ticket



LOGIN_URL='http://127.0.0.1:8000/register/log_in'


@login_required(login_url=LOGIN_URL)
def CreateChatSupport(request: HttpRequest): 
    username = request.user
    id_ticket = random_id_ticket()
    print(id_ticket)
    return render(
    request, 'CreateSupportChat.html', 
    {'username': username, 'id_ticket': id_ticket}
    )

@login_required(login_url=LOGIN_URL)
def ChatSupport(request: HttpRequest):
    username = request.GET.get('username')
    id_ticket = request.GET.get('id_ticket')
    print(username)
    print(id_ticket)

    time = datetime.today()
    if request.user.is_staff is True:
        print(request.user)
        cache_id_ticket.append(id_ticket)
        DataTicket.objects.filter(id_ticket=id_ticket).update(accept_staff_name=request.user.username, date_accept_ticket=time)
        return render(request, 'SupportChat.html', {'username': request.user.username, 'id_ticket': id_ticket})
    else:
        check_username_db = DataTicket.objects.filter(username_create_ticket=request.user.username)
        print(check_username_db)
        if check_username_db:
            id_ticket = DataTicket.objects.get(username_create_ticket=request.user.username).id_ticket
            print(id_ticket)
            cache_id_ticket.append(id_ticket)
            return render(request, 'SupportChat.html', {'username': request.user.username})
    
        DataTicket.objects.create(
            id_ticket=id_ticket,
            username_create_ticket=username,
            date_create_ticket=time
            )
        
        cache_id_ticket.append(id_ticket)
        return render(request, 'SupportChat.html', {'username': username})



    
@login_required(login_url=LOGIN_URL)
def modoretor_SupportChat(request: HttpRequest):
    pass