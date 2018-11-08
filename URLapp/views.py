from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import F
# Create your views here.


def get_new_url(request):
    short_url = None

    if request.method == "POST":
        link_db = URLModels
        link_db.original_url = request.POST.get("url")
        link_db.save()
        short_url = request.build_absolute_uri(link_db.get_short_url())

    return render(request, 'home.html', {'short_url': short_url})


def get_original_url(request, id):
    link_id = URLModels.decode_url(id)
    link_db = get_object_or_404(URLModels, url_id=link_id)
    link_db.update(hits=F('hits') + 1)

