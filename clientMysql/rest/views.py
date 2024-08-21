from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer, PktRecordLogSerializer, PktreaderSerializer
from index.models import PktRecordLog, Pktreader

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PktRecordLogViewSet(viewsets.ModelViewSet):
    queryset = PktRecordLog.objects.all().order_by('time')
    serializer_class = PktRecordLogSerializer
    # permission_classes = [permissions.IsAuthenticated]

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
