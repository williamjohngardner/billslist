from django.shortcuts import render
from rest_framework import generics
from app.models import Category, SubCategory, Listing, Region, Profile
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from restful.serializers import CategorySerializer, SubCategorySerializer, ListingSerializer, RegionSerializer, ProfileSerializer
from restful.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response



class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListingListAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        list = self.kwargs.get('pk', None)
        return Listing.objects.filter(category=list)

class SubCategoryListingListAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        list = self.kwargs.get('pk', None)
        return Listing.objects.filter(subcategory=list)

class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ListingListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)

class ListingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsOwnerOrReadOnly)

class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ProfileListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
