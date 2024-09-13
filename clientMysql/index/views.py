from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .models import Pktreader, worker
from .forms import addForm

# Create your views here.

def index(request):
    return render(request, "index/index.html")


def logs(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "sub":
            form = addForm(request.POST)
            if form.is_valid():
                form.save()

    items = Pktreader.objects.all().order_by("time")
    names = worker.objects.all().order_by("id")

    params = {
        "names": names,
        "items": items,
        "form": form,

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





# def formadd(request):
#     if request.method == "POST":
#         form = addForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'logs.html', {'form':form})
def addPost(request):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("/Addr.html")
def getform(request):

    if request.method == 'GET':
        action = request.GET.get("action")
        if action == "sub":
            form = addForm(initial={"mac_addr": request.GET.get("mac_addr", "---")})
        # if action == "EditUser":
        #     user_id = request.GET.get("id")
        #     args = Person.objects.get_person_info(user_id)
        #     form = UserFormEdit(initial=args)
        # if action == "DeleteUser":
        #     user_id = request.GET.get("id")
        #     args = {"id": user_id}
        #     form = DeleteUserForm(initial=args)

    params = {
        "form": form,

    }
    return render(request, "index/Addr/add.html", params)
def add(request):
    form = addForm(initial={"mac_addr": request.GET.get("mac_addr", "---")})

    params = {
        "form": form,
    }
    return render(request, "index/logs.html", params)
