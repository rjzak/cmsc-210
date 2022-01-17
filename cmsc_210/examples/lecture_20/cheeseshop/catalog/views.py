from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Cheese


def cheese_list(request):
    cheeses = Cheese.objects.all()
    return render(request, "cheese_list.html", {"cheeses": cheeses})


def cheese_detail(request, cheese_id):
    cheese = get_object_or_404(Cheese, slug=cheese_id)
    return render(request, "cheese_detail.html", {"cheese": cheese})
