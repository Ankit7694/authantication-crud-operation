from django.db import models

# Create your models here.
class Details(models.Model):
    city_name=models.CharField(max_length=200, default="")
    state_name=models.CharField(max_length=200,default="")
    country_name=models.CharField(max_length=200,default="")
    image= models.ImageField(upload_to='static/images', default="")

    def __str__(self):
        return self.city_name