from django.http import HttpResponse
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pktreader, worker
from .forms import addForm, addFormAddr, delFormAddr

# Create your views here.

def index(request):
    return render(request, "index/index.html")


def logs(request):
    error = ""
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "sub":
            form = addForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = form.errors

    items = Pktreader.objects.all().order_by("time")
    names = worker.objects.all().order_by("id")

    params = {
        "names": names,
        "items": items,
        "error":error,

        "title": f"всего компов"
    }
    return render(request, "index/logs.html", params)

def delete(request, pk):
    addrs = get_object_or_404(worker, pk=pk)
    addrs.delete()

def addr(request):
    error = ""
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "addrdel":
            id = request.POST.get("id")
            obj = worker.objects.get(id=id)
            obj.delete()
        if action == "subAddr":
            form = addFormAddr(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = form.errors
    names = worker.objects.all().order_by("id")
    params = {
        "names": names,
        "eror": error,
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
        if action == "subAddr":
            form = addFormAddr()
        if action == "delAddr":
            id = request.GET.get("id", False)
            if id:
                obj = worker.objects.get(id=id)
                form = delFormAddr(instance=obj)


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
