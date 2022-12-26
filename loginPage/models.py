from django.db import models

# Create your models here.

class Zakaznik(models.Model):
    nazov_firmy = models.CharField(max_length=100)

    def __str__(self):
        return self.nazov_firmy