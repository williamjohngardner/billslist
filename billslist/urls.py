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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout

from app.views import IndexPageView, RegionsPageView, CategoryPageView, SubcategoryPageView, ListingDetailView, ProfilePageView, PostNewListingView, ListingPageView, CreateUserView, CityListPageView
from app.views import ListingSortedCreated
from restful.views import CategoryListAPIView, CategoryDetailAPIView, SubCategoryListAPIView, SubCategoryDetailAPIView, ListingListAPIView, ListingDetailAPIView
from restful.views import RegionListAPIView, RegionDetailAPIView, ProfileListAPIView, ProfileDetailAPIView, CategoryListingListAPIView, SubCategoryListingListAPIView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexPageView.as_view(), name="index_page_view"),
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user"),
    url(r'^accounts/profile/$', login_required(ProfilePageView.as_view()), name="profile_page_view"),
    url(r'^regions/$', RegionsPageView.as_view(), name="regions_page_view"),
    url(r'^city_list/(?P<pk>\w+)/$', CityListPageView.as_view(), name="city_list_page_view"),
    url(r'^(?P<pk>\d+)/$', SubcategoryPageView.as_view(), name="subcategory_page_view"),
    url(r'^listing/$', ListingPageView.as_view(), name="listing_page_view"),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name="listing_detail_view"),
    url(r'^listing/(?P<pksub>\d+)/created/$', ListingSortedCreated.as_view(), name="listing_sorted_created"),
    url(r'^post_new_listing/$', login_required(PostNewListingView.as_view()), name="post_new_listing_view"),
    url(r'^(?P<category>\w+)/$', CategoryPageView.as_view(), name="category_page_view"),

    url(r'^api/category/$', CategoryListAPIView.as_view(), name="category_list_api_view"),
    url(r'^api/category/(?P<pk>\d+)/$', CategoryDetailAPIView.as_view(), name="category_detail_api_view"),
    url(r'^api/category/(?P<pk>\d+)/listing/$', CategoryListingListAPIView.as_view(), name='category_listing_list_api_view'),
    url(r'^api/sub_category/(?P<pk>\d+)/listing/$', SubCategoryListingListAPIView.as_view(), name='sub_category_listing_list_api_view'),
    url(r'^api/sub_category/$', SubCategoryListAPIView.as_view(), name="sub_category_list_api_view"),
    url(r'^api/sub_category/(?P<pk>\d+)/$', SubCategoryDetailAPIView.as_view(), name="sub_category_detail_api_view"),
    url(r'^api/listing/$', ListingListAPIView.as_view(), name="listing_list_api_view"),
    url(r'^api/listing/(?P<pk>\d+)/$', ListingDetailAPIView.as_view(), name="listing_detail_api_view"),
    url(r'^api/region/$', RegionListAPIView.as_view(), name="region_list_api_view"),
    url(r'^api/region/(?P<pk>\d+)/$', RegionDetailAPIView.as_view(), name="region_detail_api_view"),
    url(r'^api/profile/$', ProfileListAPIView.as_view(), name="profile_list_api_view"),
    url(r'^api/profile/(?P<pk>\d+)/$', ProfileDetailAPIView.as_view(), name="profile_detail_api_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
