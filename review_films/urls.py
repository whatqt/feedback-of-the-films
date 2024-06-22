from django.urls import path
from . import views



urlpatterns = [
    path("", views.select_films),
    path("feedback_film", views.feedback_films),
    path("views_feedback", views.views_feedback_films),
    path('have_review', views.have_review),
    path('view_feedback', views.view_feedback),
    path('my_review', views.my_review),
    path('editing_my_review', views.editing_my_review)
]