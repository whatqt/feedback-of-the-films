from django.db import models

class DataTicket(models.Model):
    id_ticket = models.CharField(null=False, primary_key=True)
    username_create_ticket = models.CharField(null=True)
    date_create_ticket = models.DateTimeField(null=True)
    accept_staff_name = models.CharField(null=True)
    date_accept_ticket = models.DateTimeField(null=True) 

class DataClosedTicket(models.Model):
    id_ticket = models.CharField(null=False)
    username_create_ticket = models.CharField(null=True)
    date_create_ticket = models.DateTimeField(null=True)
    accept_staff_name = models.CharField(null=True)
    date_accept_ticket = models.DateTimeField(null=True) 
    date_closed_ticket = models.DateTimeField(null=True)
