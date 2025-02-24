from django.db import models

# Create your models here.

class Autor(models.Model):
    img = models.ImageField(upload_to='autori/', verbose_name="Fotka autora", blank=True, null=True)
    jmeno = models.CharField(max_length=100, verbose_name="Jméno autora")
    narozen = models.DateField(verbose_name="Datum narození", blank=True, null=True)
    umrti = models.DateField(verbose_name="Datum úmrtí", blank=True, null=True)
    zivotopis = models.TextField(verbose_name="Životopis", blank=True, null=True)
    
    def __str__(self):
        return f"{self.jmeno}"

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autoři"