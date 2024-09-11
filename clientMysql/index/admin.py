from django.contrib.admin import ModelAdmin, register
from .models import *


@register(PktRecordLog)
class PktRecordLogAdmin(ModelAdmin):
    list_display = ("time", "type", "data")
    search_fields = ('data', 'time')
    list_filter = ("time", )

@register(Pktreader)
class PktreaderAdmin(ModelAdmin):
    # pass
    list_display = ("mac_addr", "ip_addr", "time")
    search_fields = ('mac_addr', 'ip_addr')

@register(worker)
class WorkerAdmin(ModelAdmin):
    list_display = ("name", "mac_addr", "data")
    search_fields = ('mac_addr', 'name')
    list_filter = ("mac_addr")

