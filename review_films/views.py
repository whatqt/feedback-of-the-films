from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.db.utils import IntegrityError, ProgrammingError
from .models import Test_DataFullInfoFilms, Test_UserReview
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .parser import get_info_films
from datetime import datetime



LOGIN_URL='http://127.0.0.1:8000/register/log_in'


@login_required(login_url=LOGIN_URL)
def select_films(request: HttpRequest):
    if request.method == 'POST':
        movie_name_post = request.POST.get('movie_name')
        films_dict = {}
        list_names_films = []
        get_info_films(movie_name_post, films_dict, list_names_films)
        # print(films_dict)
        context_data = {'films_dict': films_dict, 'movie_name_post': movie_name_post}
        return render(request, 'output_films_base.html', context=context_data)
    return render(request, 'select_films_base.html')

@login_required(login_url=LOGIN_URL)
def feedback_films(request: HttpRequest):
    print(request.method)
    if request.method == 'GET':
        movie_title_get = request.GET.get('movie_title')
        movie_authors_get = request.GET.get('movie_authors')
        brief_information_get = request.GET.get('brief_information')
        film_info_list = Test_DataFullInfoFilms.objects.filter(
            movie_title=movie_title_get,
            movie_authors=movie_authors_get,
            brief_informatio=brief_information_get
        ).values('movie_title', 'brief_informatio')

        print(film_info_list)
        if film_info_list:
            pass
        else:
            Test_DataFullInfoFilms.objects.create(
                movie_title=movie_title_get,
                movie_authors=movie_authors_get,
                brief_informatio=brief_information_get
            )
            with connection.cursor() as cursor:
                id_film = Test_DataFullInfoFilms.objects.filter(
                    movie_title=movie_title_get,
                    movie_authors=movie_authors_get,
                    brief_informatio=brief_information_get
                ).values_list('id', flat=True)
                print(id_film)
                try:
                    cursor.execute(f"""
                    CREATE TABLE film_{id_film[0]}
                    (
                        username varchar(20) PRIMARY KEY,
                        time_movie_review timestamp without time zone,
                        movie_review varchar(400)
                    );                     
                    """)
                except ProgrammingError:
                    pass
            print(movie_title_get)
            data_context = {'movie_title': movie_title_get, 'movie_authors': movie_authors_get}
            return render(request, 'feedback_film_base.html', context=data_context)
        
        data_context = {'movie_title': movie_title_get ,'movie_authors': movie_authors_get}
        return render(request, 'feedback_film_base.html', context=data_context)
    elif request.method == 'POST':
        username = request.user
        movie_title_post = request.POST.get('movie_title')
        movie_authors_post = request.POST.get('movie_authors')
        brief_information_post = request.GET.get('brief_information')
        movie_review_post = request.POST.get('movie_review')
        print(movie_title_post)
        print(movie_review_post)
        
        id_film = Test_DataFullInfoFilms.objects.filter(
            movie_title=movie_title_post,
            movie_authors=movie_authors_post,
            brief_informatio=brief_information_post
        ).values_list('id', flat=True)

        print(id_film)
        movie_title = f'film_{id_film[0]}'
        time = datetime.today()
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"""
            INSERT INTO  {movie_title}
            VALUES ('{username}', TIMESTAMP '{time}', '{movie_review_post}')
                """)
        except IntegrityError:
            return HttpResponse('У вас уже есть рецензия на этот фильм')

        Test_UserReview.objects.create(
            username=username,
            movie_title=movie_title_post,
            movie_authors=movie_authors_post,
            brief_informatio=brief_information_post,
            movie_review=movie_review_post,
            time_movie_review=time
            )
        return HttpResponse('<h1>Ваша рецензия была добавлена</h1>')


@login_required(login_url=LOGIN_URL)
def have_review(request: HttpRequest):
    films = Test_DataFullInfoFilms.objects.values_list('movie_title', 'movie_authors', 'brief_informatio')
    print(films)
    data = {}
    number_film = 1
    for data_film in films:
        data[number_film] = data_film
        number_film+=1
    print(data)
    return render(request, 'have_review_base.html', context={'data': data})

@login_required(login_url=LOGIN_URL)    
def view_feedback(request: HttpRequest):
    print(request.method)
    if request.method == 'GET':
        movie_title_get = request.GET.get('movie_title')
        movie_authors_get = request.GET.get('movie_authors')
        brief_information_get = request.GET.get('brief_information')
        print(f'{movie_title_get}\n{movie_authors_get}\n{brief_information_get}')
        film = Test_DataFullInfoFilms.objects.filter(
            movie_title=movie_title_get,
            movie_authors=movie_authors_get,
            brief_informatio=brief_information_get
            )
        print(film)
        film_id = film.values_list('id', flat=True)
        print(film_id)
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT * FROM film_{film_id[0]}
            """)
            info_reviews= cursor.fetchall()
        print(info_reviews)
        review_data = {}
        film_data = film.values_list('movie_title','movie_authors','brief_informatio')[0]
        print(film_data)
        number_review = 1
        for info in info_reviews:
            review_data[number_review] = info
            number_review+=1

        return render(request, 'view_feedback_base.html', {'review_data': review_data, 'film_data': film_data})
    

@login_required(login_url=LOGIN_URL)
def my_review(request: HttpRequest):
    user = request.user
    info = Test_UserReview.objects.all()
    user_review = info.filter(username=user).values_list('movie_title','movie_authors','brief_informatio', 'movie_review','time_movie_review')
    print(user_review)
    return render(request, 'my_review_base.html', {'data': user_review})

@login_required(login_url=LOGIN_URL)
def editing_my_review(request: HttpRequest):
    if request.method == 'GET':
        movie_title_get = request.GET.get('movie_title')
        movie_authors_get = request.GET.get('movie_authors')
        brief_information_get = request.GET.get('brief_information')
        data = {'movie_title': movie_title_get, 'movie_authors': movie_authors_get, 'brief_information': brief_information_get}
        return render(request, 'editing_my_review_base.html', data)
    elif request.method == 'POST':
        movie_title_get = request.GET.get('movie_title')
        movie_authors_get = request.GET.get('movie_authors')
        brief_information_get = request.GET.get('brief_information')
        editing_review_post = request.POST.get('editing_review')
        print(movie_title_get)
        print(movie_authors_get)
        print(brief_information_get)
        print(editing_review_post)

        id_film = Test_DataFullInfoFilms.objects.filter(
            movie_title=movie_title_get,
            movie_authors=movie_authors_get,
            brief_informatio=brief_information_get
        ).values_list('id', flat=True)
        print(id_film[0])
        with connection.cursor() as cursor:
            cursor.execute(f"""
            UPDATE film_{id_film[0]}
            SET movie_review = '{editing_review_post}'
            """)

        Test_UserReview.objects.filter(
            movie_title=movie_title_get,
            movie_authors=movie_authors_get,
            brief_informatio=brief_information_get
            ).update(movie_review=editing_review_post)
        
        return redirect('http://127.0.0.1:8000/select_films/my_review')  
    
