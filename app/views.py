from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView



class IndexPageView(TemplateView):
    template_name = "index.html"


class RegionsPageView(TemplateView):
    pass


class CategoryPageView(TemplateView):
    pass


class SubcategoryPageView(TemplateView):
    pass


class ListingPageView(ListView):
    # template_name = listing.html
    pass

class ProfilePageView(TemplateView):
    pass


class PostNewListingView(TemplateView):
    pass
