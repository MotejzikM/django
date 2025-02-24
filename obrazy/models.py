from django.db import models
from autori.models import Autor

# Create your models here.

class Obraz(models.Model):
    img = models.ImageField(upload_to='obrazy/', verbose_name="Obrázek", blank=True, null=True)
    nazev = models.CharField(max_length=100, verbose_name="Název obrazu")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor obrazu", null=True, blank=True)
    rok = models.IntegerField(verbose_name="Rok", null=True, blank=True)
    technika = models.ForeignKey('Technika', on_delete=models.CASCADE, verbose_name="Technika", null=True, blank=True)
    poznamky = models.TextField(verbose_name="Poznámky", null=True, blank=True)
    cena = models.IntegerField(verbose_name="Cena obrazu", null=True, blank=True)

    def __str__(self):
        return f"{self.nazev} ({self.autor}, {self.rok})"
    
    class Meta:
        verbose_name = "Obraz"
        verbose_name_plural = "Obrazy"


class Technika(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název techniky")

    def __str__(self):
        return self.nazev
    
    class Meta:
        verbose_name = "Technika"
        verbose_name_plural = "Techniky"