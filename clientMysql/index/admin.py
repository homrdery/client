from django.contrib.admin import ModelAdmin, register
from .models import *


@register(PktRecordLog)
class PktRecordLogAdmin(ModelAdmin):
    list_display = ("time", "type", "data")


@register(Pktreader)
class PktreaderAdmin(ModelAdmin):
    # pass
    list_display = ("mac_addr", "ip_addr", "time")
    search_fields = ('mac_addr', 'ip_addr')
