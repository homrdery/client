from django.contrib.auth.models import Group, User
from rest_framework import serializers
from index.models import PktRecordLog, Pktreader, worker
from directory.models import dirAddr

class PktRecordLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PktRecordLog
        fields = "__all__"

class PktreaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pktreader
        fields = "__all__"

class workerSerializer(serializers.ModelSerializer):
    class Meta:
        model = worker
        fields = "__all__"

class dirAddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = dirAddr
        fields = "__all__"