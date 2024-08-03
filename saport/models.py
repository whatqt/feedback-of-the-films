from django.db import models

class InfoTicket(models.Model):
    id_ticket = models.CharField(primary_key=True, max_length=30),
    username_create_ticket = models.CharField(max_length=30),
    date_create_ticket = models.DateTimeField()
