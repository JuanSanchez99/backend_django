from django.db import models


# Create your models here.
class Person(models.Model):
    DOCUMENT_TYPES = (
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tarjeta de Identidad'),
    )
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPES)
    document_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200)
