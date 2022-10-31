from django.db import models

# Create your models here.
class Product_master(models.Model):
    product_name = models.CharField(max_length=50,unique=True)
    category_name = models.CharField(max_length=5,default="")
    def __str__(self):
        return self.product_name + " / " + self.category_name