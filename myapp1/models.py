from django.db import models
from datetime import datetime

# Create your models here.
class Product_master(models.Model):
    product_name = models.CharField(max_length=50,unique=True)
    category_name = models.CharField(max_length=5,default="")
    def __str__(self):
        return self.product_name + " / " + self.category_name

class Waste_item_master_list(models.Model):
    waste_item_code = models.CharField(max_length=9,unique=True)
    description_EN = models.CharField(max_length=50,default="")
    description_TH = models.CharField(max_length=100,default="")
    waste_group_code = models.CharField(max_length=5,default="")
    systems_date = models.DateField(default=datetime.now)
    update_date = models.CharField(max_length=20,default="")
    update_by = models.CharField(max_length=100,default="")
