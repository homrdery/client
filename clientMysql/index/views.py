from django.http import HttpResponse
from django.shortcuts import render
from .models import Pktreader, worker
from .forms import addForm

# Create your views here.

def index(request):
    return render(request, "index/index.html")


def logs(request):
    items = Pktreader.objects.all().order_by("time")
    names = worker.objects.all().order_by("id")
    params = {
        "names": names,
        "items": items,
        "title": f"всего компов"
    }
    return render(request, "index/logs.html", params)


def computers(request):
    items = Pktreader.objects.all().order_by("time")
    names = worker.objects.all().order_by("id")
    params = {
        "names": names,
        "items": items,
        "title": f"всего компов"
    }
    return render(request, "index/page.html")


def addr(request):
    names = worker.objects.all().order_by("id")
    params = {
        "names": names,
        "title": f"всего компов"
    }
    return render(request, "index/Addr.html", params)


def add(request):
    form = addForm(initial={"mac_addr": request.GET.get("mac_addr", "---")})

    params = {
        "form": form,
    }
    return render(request, "index/Addr/add.html", params)
