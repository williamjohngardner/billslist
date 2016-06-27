from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from app.models import SubCategory, Category, Listing, Profile, Region
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['listing_list'] = Listing.objects.all()
        return context


class CreateUserView(CreateView):
    model = Profile
    form_class = UserCreationForm
    success_url = "/login"


class RegionsPageView(ListView):
    model = Region


class CityListPageView(ListView):
    model = Listing

    def get_queryset(self, **kwargs):
        city = self.kwargs.get('pk', None)
        return Listing.objects.filter(location=city)


class CategoryPageView(TemplateView):
    pass


class SubcategoryPageView(ListView):
    model = Listing

    def get_queryset(self, **kwargs):
        sub = self.kwargs.get('pk', None)
        return Listing.objects.filter(subcategory=sub)


class ListingPageView(ListView):
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing_list'] = Listing.objects.all()
        context['sorted_newest'] = Listing.objects.all().order_by('-created')
        context['sorted_price'] = Listing.objects.all().order_by('-price')
        return context


class ListingSortedCreated(ListView):
    model = Listing
    template_name = "listing_list.html"

    def get_queryset(self, **kwargs):
        pksub = self.kwargs.get('pksub', None)
        return Listing.objects.filter(pk=pksub)


class ListingDetailView(DetailView):
    model = Listing



class ProfilePageView(UpdateView):
    # template_name = "accounts/profile.html"
    fields = ["first_name", "last_name", "location_pref", "zip_code", "photo"]
    model = Profile
    success_url = reverse_lazy("index_page_view")

    def get_object(self, queryset=None):
        return self.request.user


class PostNewListingView(CreateView):
    model = Listing
    fields = ["title", "price", "location", "subcategory", "photos", "description", "post_id", "profile"]
