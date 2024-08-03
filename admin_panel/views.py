from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User



def index_admin(request: HttpRequest):
    username = request.user.username
    check_staff = User.objects.filter(username=username).values()[0]
    if check_staff['is_staff'] is True:
        return HttpResponse("Добро пожаловать в панель администратора")
