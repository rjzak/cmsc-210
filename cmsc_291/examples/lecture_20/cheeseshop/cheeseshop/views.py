from datetime import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render

from cheeseshop.cheeses import CHEESES


def index(request):
    now = datetime.now()
    return render(request, "index.html", {"now": now})

def cheese_list(request):
    cheeses = sorted([(slug, name, country) for slug, (name, country, _) in CHEESES.items()])
    return render(request, "cheese_list.html", {"cheeses": cheeses})


def cheese_detail(request, cheese_id):
    if cheese_id not in CHEESES:
        return HttpResponseNotFound(f"I don't know about a cheese called {cheese_id}.")
    name, country, description = CHEESES[cheese_id]
    return render(request, "cheese_detail.html", {"name": name, "country": country, "description": description})
