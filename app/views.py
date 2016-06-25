from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from app.models import SubCategory, Category, Listing, Profile
from django.contrib.auth.forms import UserCreationForm


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


class RegionsPageView(TemplateView):
    pass


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
        return context


class ListingDetailView(DetailView):
    model = Listing


class ProfilePageView(UpdateView):
    # template_name = "accounts/profile.html"
    fields = ["first_name", "last_name", "street_address", "street_address_2", "city", "state", "zip_code", "email", "photo"]
    model = Profile

    def get_object(self, queryset=None):
        return self.request.user


class PostNewListingView(CreateView):
    model = Listing
    fields = ["title", "price", "location", "subcategory", "photos", "description", "post_id", "profile"]
