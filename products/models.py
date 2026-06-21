from django.db import models

class Cateogory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Cateogory, on_delete=models.CASCADE) #taking category as foreign key
    name=models.CharField(max_length=100)
    price=models.DecimalField( max_digits=10, decimal_places=2)
    description=models.TextField(max_length=200)
    image=models.ImageField(upload_to="products/")
    def __str__(self):
        return self.name


# Create your models here.
