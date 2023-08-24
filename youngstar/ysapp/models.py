from django.db import models


# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name