from django.db import models


class Test_accounts(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(null=None)

