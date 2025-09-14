from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(Max_lengt=250)