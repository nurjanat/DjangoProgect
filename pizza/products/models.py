from django.db import models

# Create your models here.
class Product(models.Model):
    categories = (
        ('vegan','vegan'),
        ('not_vegan','chile'),
    )
    sizes = (
        ('small','small'),
        ('middle','middle'),
        ('great','great')
    )
    image = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20,choices=categories)
    description = models.TextField(blank=True)
    price = models.FloatField()
    size = models.CharField(choices=sizes,max_length=50)





class AboutUs(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()



class Contacts(models.Model):
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    time = models.CharField(max_length=15)
    mng_name = models.CharField(max_length=12)