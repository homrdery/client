from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import  PktRecordLogSerializer, PktreaderSerializer
from index.models import PktRecordLog, Pktreader

class PktRecordLogViewSet(viewsets.ViewSet):
    queryset = PktRecordLog.objects.all().order_by('time')
    serializer_class = PktRecordLogSerializer
    permission_classes = [permissions.IsAuthenticated]

class PktreaderViewSet(viewsets.ModelViewSet):
    queryset = Pktreader.objects.all().order_by('time')
    serializer_class = PktreaderSerializer
    permission_classes = [permissions.IsAuthenticated]


def page(request):
    items = Pktreader.objects.all().order_by("time")
    params = {
        "items": items,
        "title": f"всего компов"
    }
    return render(request, "index/page.html", params)
