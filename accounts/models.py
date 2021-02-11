from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    usrname = models.CharField(max_length=100)
    status = models.CharField(max_length=200, default="inactive")

    def __str__(self):
        return self.first_name
