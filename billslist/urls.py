"""billslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from app.views import IndexPageView, RegionsPageView, CategoryPageView, SubcategoryPageView, ListingDetailView, ProfilePageView, PostNewListingView, ListingPageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexPageView.as_view(), name="index_page_view"),
    url(r'^regions/$', RegionsPageView.as_view(), name="regions_page_view"),
    url(r'^(?P<pk>\d+)/$', SubcategoryPageView.as_view(), name="subcategory_page_view"),
    url(r'^listing/$', ListingPageView.as_view(), name="listing_page_view"),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name="listing_detail_view"),
    url(r'^accounts/profile/$', ProfilePageView.as_view(), name="profile_page_view"),
    url(r'^post_new_listing/$', PostNewListingView.as_view(), name="post_new_listing_view"),
    url(r'^(?P<category>\w+)/$', CategoryPageView.as_view(), name="category_page_view"),
]
