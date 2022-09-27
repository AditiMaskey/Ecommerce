from email.policy import default
from tkinter.messagebox import NO
from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product ,default=None, on_delete=models.PROTECT)
    images = models.ImageField(upload_to = 'photos/products', default=None)
    
    def __str__(self):
        return self.product.name