from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=300)
    usn = models.CharField(max_length=100,primary_key = True)
    branch = models.CharField(max_length=200)

    