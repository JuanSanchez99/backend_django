from django.db import models


# Create your models here.
class People(models.Model):
    DOCUMENT_TYPES = (
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tarjeta de Identidad'),
    )
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPES)
    document_id = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    hobbie = models.CharField(max_length=200)
