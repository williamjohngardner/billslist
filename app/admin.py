from django.contrib import admin
from app.models import Category, Listing, SubCategory, Profile


admin.site.register(Category)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'category')

admin.site.register(SubCategory, SubcategoryAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'zip_code')

admin.site.register(Profile, ProfileAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'subcategory', 'created')

admin.site.register(Listing, ListingAdmin)
