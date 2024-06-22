from django.db import models


class Test_DataFullInfoFilms(models.Model):
    movie_title = models.CharField()
    movie_authors = models.CharField()
    brief_informatio = models.CharField()

class Test_UserReview(models.Model):
    username = models.CharField()
    movie_title = models.CharField()
    movie_authors = models.CharField()
    brief_informatio = models.CharField()
    movie_review = models.CharField()
    time_movie_review = models.DateTimeField()