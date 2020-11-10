from django.shortcuts import render, get_object_or_404

from .models import Cheese


def cheese_list(request):
    cheeses = Cheese.objects.all()
    return render(request, "cheese_list.html", {"cheeses": cheeses})


def cheese_detail(request, cheese_id):
    cheese = get_object_or_404(Cheese, slug=cheese_id)
    return render(request, "cheese_detail.html", {"cheese": cheese})
