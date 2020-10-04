
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('auctions.urls')),
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
]