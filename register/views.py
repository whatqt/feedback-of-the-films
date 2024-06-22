from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .editing_password import password_to_hash
from .models import Test_accounts
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index_home(request: HttpRequest):
    return HttpResponse('Главная страница')

def index_reg(request: HttpRequest):
    return HttpResponse('Домашняя страница регистрации')

def log_in(request: HttpRequest):
    if request.method == 'POST':
        try:
            user_name_post = request.POST.get('username').replace(' ', '')
            password_post = password_to_hash(request.POST.get('password').replace(' ', ''))
            # Test_accounts.objects.create(username=user_name_post, password=password_post)
            print(user_name_post)
            print(password_post)
            data_user = Test_accounts.objects.filter(username=user_name_post).values()[0]
            print(data_user)
            if data_user['password'] == password_post:
                user = authenticate(request, username=user_name_post, password=password_post)
                print(user)
                login(request, user)
                return redirect('/select_films/')
            else:
                return HttpResponse(f'Неправильный пароль или логин')
        except IntegrityError:
            return HttpResponse(f'<h1>Ник {user_name_post} уже занят</h1>')
        except IndexError:
            return HttpResponse(f'<h1>Аккаунт с ником {user_name_post}не найден/h1>')
    else:
        return render(request, 'log_in.html')

def register(request: HttpRequest):
    if request.method == 'POST':
        user_name_post = request.POST.get('username').replace(' ', '')
        password_post = password_to_hash(request.POST.get('password').replace(' ', ''))
        Test_accounts.objects.create(username=user_name_post, password=password_post)
        User.objects.create_user(user_name_post, None, password_post)
        return redirect('/register/log_in')
    else:
        if request.user.is_anonymous is False:
            return HttpResponse('Нет доступа', status=400)
        else:
            print(request.user)
            print(request.user.is_anonymous)            
            return render(request, 'register.html')

@login_required(login_url='/register/log_in')
def films(request: HttpRequest):
    return HttpResponse('Здесь будут фильмы')

@login_required(login_url='/register/log_in')
def log_out(request: HttpRequest):
    logout(request)
    return HttpResponse('Вы вышли из системы')


