from rest_framework import serializers
from app.models import Category, SubCategory, Listing, Region, Profile


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category']

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='category_detail_api_view'
    )

    class Meta:
        model = SubCategory
        fields = ['subcategory', 'category']

class ListingSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='category_detail_api_view'
    )
    subcategory = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='sub_category_detail_api_view'
    )

    location = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='region_detail_api_view'
    )

    profile = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='profile_detail_api_view'
    )

    class Meta:
        model = Listing
        fields = ['title', 'price', 'location', 'category', 'subcategory', 'photos', 'created', 'description', 'post_id', 'profile']

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['location']

class ProfileSerializer(serializers.ModelSerializer):
    location_pref = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='region_detail_api_view'
    )

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'street_address', 'street_address_2', 'city', 'state', 'zip_code', 'email', 'location_pref', 'photo']
