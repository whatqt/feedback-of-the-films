from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index_home(request: HttpRequest):
    return HttpResponse('Главная страница')

def log_in(request: HttpRequest):
    if request.method == 'POST':
        try:
            user_name_post = request.POST.get('username').replace(' ', '')
            password_post = request.POST.get('password').replace(' ', '')
            print(user_name_post)
            print(password_post)          
            user = authenticate(request, username=user_name_post, password=password_post)
            print(user)
            login(request, user)
            if request.user.is_staff is True:
                return redirect('/admin_panel/')
            else:
                return redirect('/select_films/')
        except (IndexError, AttributeError):
            return HttpResponse(f'<h1>Неверный логин или пароль!</h1>')
    else:
        return render(request, 'log_in.html')

def register(request: HttpRequest):
    if request.method == 'POST':
        user_name_post = request.POST.get('username').replace(' ', '')
        password_post = request.POST.get('password').replace(' ', '')
        check_repeat_name = User.objects.filter(username=user_name_post)
        print(check_repeat_name)
        if check_repeat_name:
            return HttpResponse('<h1>Такой ник уже занят</h1>')            
        User.objects.create_user(user_name_post, None, password_post)
        return redirect('/register/log_in')
    else:
        if request.user.is_anonymous is False:
            return HttpResponse('<h1>Нет доступа</h1>', status=400)
        else:
            print(request.user)
            print(request.user.is_anonymous)            
            return render(request, 'register.html')

@login_required(login_url='/register/log_in')
def films(request: HttpRequest):
    return HttpResponse('<h1>Здесь будут фильмы</h1>')

@login_required(login_url='/register/log_in')
def log_out(request: HttpRequest):
    logout(request)
    return HttpResponse('<h1>Вы вышли из системы</h1>')


