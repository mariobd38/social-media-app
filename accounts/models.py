from curses import raw
from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    username = models.TextField()
    password = models.TextField()
    phone_number = models.TextField(blank=True)
    dob = models.DateField()
    gender = models.TextField()

