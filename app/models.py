from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2)
    location = models.CharField(max_length=60)
    photos = models.ImageField()
    email = models.EmailField()
    created = models.DateTimeField()
    description = models.TextField()
    post_id = models.IntegerField()


class Category(models.Model):
    category = models.CharField()


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=20)
