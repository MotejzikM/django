from django.db import models

# Create your models here.

class Obraz(models.Model):
    img = models.ImageField(upload_to='obrazy/')
    nazev = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    rok = models.IntegerField()
    technika = models.CharField(max_length=100)
    poznamky = models.TextField()
    cena = models.IntegerField()