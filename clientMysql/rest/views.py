from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import PktRecordLogSerializer, PktreaderSerializer
from index.models import PktRecordLog, Pktreader


class PktRecordLogViewSet(viewsets.ModelViewSet):
    queryset = PktRecordLog.objects.all().order_by('time')
    serializer_class = PktRecordLogSerializer

    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post", ], url_path=r'bulk_post')
    def bulk_post(self, request):
        count = 0
        for obj in request.POST.get("data", []):
            count += 1
        return Response({"count": count}, status=HTTP_200_OK)


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
