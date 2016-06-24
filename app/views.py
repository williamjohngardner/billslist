from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from app.models import SubCategory, Category, Listing, Profile
from django.contrib.auth.forms import UserCreationForm


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class CreateUserView(CreateView):
    model = Profile
    form_class = UserCreationForm
    success_url = "/"


class RegionsPageView(TemplateView):
    pass


class CategoryPageView(TemplateView):
    pass


class SubcategoryPageView(ListView):
    # template_name = "listing_page.html"

    def get_queryset(self, **kwargs):
        sub = self.kwargs.get('pk', None)
        return Listing.objects.filter(subcategory=sub)


class ListingPageView(ListView):
    # template_name = "listing_page.html"
    model = Listing


class ListingDetailView(DetailView):
    model = Listing


class ProfilePageView(TemplateView):
    template_name = "accounts/profile.html"


class PostNewListingView(TemplateView):
    pass
