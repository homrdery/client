from django.http import HttpResponse
from django.shortcuts import render
from .models import Pktreader, worker

# Create your views here.

def index(request):
    return render(request, "index/index.html")

def computers(request):
    items = Pktreader.objects.all().order_by("time")
    name = worker.objects.all().order_by("time")
    params = {
        "name": name,
        "items": items,
        "title": f"всего компов"
    }
    return render(request, "index/page.html", params)
