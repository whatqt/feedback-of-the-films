from django.shortcuts import render
from django.http import HttpRequest


def ChatSaport(request: HttpRequest, name_saport_room):
    
    return render(request, 'SaportChat.html', {'name_saport_room': name_saport_room})
