from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    location = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.ForeignKey("auth.User")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    street_address_2 = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    email = models.EmailField()
    location_pref = models.ForeignKey(Region)
    photo = models.ImageField(upload_to="profile_photos", null=True, blank=True, verbose_name="Profile Photo")

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "http://www.sessionlogs.com/media/icons/defaultIcon.png"

    def __str__(self):
        return self.first_name


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=20)

    def __str__(self):
        return self.subcategory


class Listing(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Region)
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(SubCategory)
    photos = models.ImageField(upload_to="listing_photos", null=True, blank=True, verbose_name="Listing Photo")
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    post_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile)

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "http://www.sessionlogs.com/media/icons/defaultIcon.png"

    def __str__(self):
        return self.title
