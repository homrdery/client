from django.contrib.auth.models import Group, User
from rest_framework import serializers
from index.models import PktRecordLog, Pktreader

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PktRecordLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PktRecordLog
        fields = "__all__"

class PktreaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pktreader
        fields = "__all__"