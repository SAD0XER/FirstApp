from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.IntegerField()
    desc = models.TextField()
    date = models.DateField()