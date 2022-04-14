from datetime import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render
from cheeseshop.cheeses import CHEESES


def index(request):
    now = datetime.now()
    return render(request, "index.html", {"now": now})


def cheese_list(request):
    cheeses = []
    for url_name in CHEESES.keys():
        name, country, desc = CHEESES[url_name]
        cheeses.append({
            "url_name": url_name,
            "display_name": name,
            "country": country
        })
    return render(request, "cheese_list.html", {"cheeses": cheeses})


def cheese_detail(request, url_name):
    if url_name not in CHEESES:
        return HttpResponseNotFound(f"I don't know about {url_name}")
    name, country, desc = CHEESES[url_name]
    cheese = {"name": name, "country": country, "description": desc}
    return render(request, "cheese_detail.html", cheese)


"""
http://localhost:8000/cheeses/
http://localhost:8000/cheeses/cheddar/
"""
