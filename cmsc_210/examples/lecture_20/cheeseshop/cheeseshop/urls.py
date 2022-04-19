from catalog.views import cheese_detail, cheese_list
from cheeseshop.views import index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", index),
    path("cheeses/", cheese_list),
    path("cheeses/<slug:cheese_id>/", cheese_detail, name="cheese_detail"),
    path("admin/", admin.site.urls),
]
