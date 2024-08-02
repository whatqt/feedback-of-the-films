from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db import connection
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import random_id_ticket



LOGIN_URL='http://127.0.0.1:8000/register/log_in'


@login_required(login_url=LOGIN_URL)
def CreateChatSupport(request: HttpRequest): 
    username = request.user
    id_ticket = random_id_ticket()
    return render(
    request, 'CreateSupportChat.html', 
    {'username': username, 'id_ticket': id_ticket}
    )

@login_required(login_url=LOGIN_URL)
def ChatSupport(request: HttpRequest):
    if request.method == 'GET':
        username_get = request.GET.get('username')
        id_ticket_get = request.GET.get('id_ticket')
        print(username_get)
        print(id_ticket_get)

        time = datetime.today()
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'''
                CREATE TABLE {username_get}_ticket
                (   
                    id_ticket varchar(11) PRIMARY KEY,
                    username varchar(40),
                    date_create timestamp without time zone,
                    username_staf varchar(40)
                );
                INSERT INTO {username_get}_ticket
                VALUES ('{id_ticket_get}', '{username_get}', TIMESTAMP '{time}', 'None')
                ''')
            except IntegrityError:
                return HttpResponse('<h1>У вас уже есть чат</h1>', status=404)

        return render(request, 'SupportChat.html')
    
@login_required(login_url=LOGIN_URL)
def modoretor_SupportChat(request: HttpRequest):
    pass