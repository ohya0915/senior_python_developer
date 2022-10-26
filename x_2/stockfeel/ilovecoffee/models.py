from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length = 20) #coffee name
    bean_from = models.CharField(max_length = 30) #咖啡豆來源
    price = models.DecimalField(max_digits = 5, decimal_places=0) #咖啡價錢