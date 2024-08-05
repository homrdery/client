from django.http import HttpResponse
from django.shortcuts import render
from .models import Pktreader

# Create your views here.

def index(request):
    return render(request, "index/index.html")

# def computers(request):
#     items = Pktreader.objects.all().order_by("time")
#     params = {
#         "items": items,
#         "title": f"всего компов"
#     }
#     return render(request, "index/computers.html", params)
