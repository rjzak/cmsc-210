

def cheese_list(request):
    cheeses = []
    for url_name in CHEESES:
        name, country, description = CHEESES[url_name]
        cheeses.append({"url_name": url_name, "name": name, "country": country})
    return render(request, "cheese_list.html", {"cheeses": cheeses})


def cheese_detail(request, url_name):
    if url_name not in CHEESES:
        return HttpResponseNotFound(f"I don't know about a cheese called {url_name}.")
    name, country, description = CHEESES[url_name]
    return render(
        request,
        "cheese_detail.html",
        {"name": name, "country": country, "description": description},
    )
