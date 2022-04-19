"""cheeseshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cheeseshop.views import cheese_list, cheese_detail, index, get_date
from django.urls import path

urlpatterns = [
    path("", index),
    path("cheeses/", cheese_list, name="cheese_list"),
    path("cheeses/<slug:url_name>/", cheese_detail, name="cheese_detail"),
    path("date/<int:year>/", get_date),
    path("date/<int:year>/<int:month>/", get_date),
    path("date/<int:year>/<int:month>/<int:day>/", get_date),
]
