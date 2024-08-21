from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import PktRecordLogSerializer, PktreaderSerializer
from index.models import PktRecordLog, Pktreader


class PktRecordLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PktRecordLog.objects.all().order_by('time')
    serializer_class = PktRecordLogSerializer

    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post", ], url_path=r'bulk_post')
    def bulk_post(self, request):
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            count = 0
            for obj in request.data:
                count += 1
                data = obj["data"]
                if ("type" in data) and (data["type"] == 3):
                    rec = Pktreader(time=obj["time"], mac_addr=data["hwrc"], ip_addr=data["psrc"])
                    rec.save()
            return Response({"count": count}, status=HTTP_200_OK)
        else:
            return Response({"error": 1}, status=HTTP_200_OK)


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
