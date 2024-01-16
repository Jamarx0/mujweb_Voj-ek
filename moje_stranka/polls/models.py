from django.db import models
class fff(models.Model):
    autor = models.CharField(max_length=200, default="x")
    nazev = models.CharField(max_length=200, default="x")
    prispevek = models.CharField(max_length=200, default="x")
# Create your models here.
