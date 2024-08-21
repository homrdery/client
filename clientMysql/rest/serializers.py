from django.contrib.auth.models import Group, User
from rest_framework import serializers
from index.models import PktRecordLog, Pktreader


class PktRecordLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PktRecordLog
        fields = "__all__"

class PktreaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pktreader
        fields = "__all__"