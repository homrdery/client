from django.contrib.admin import ModelAdmin, register
from .models import *


@register(PktRecordLog)
class PktRecordLogAdmin(ModelAdmin):
    pass


@register(Pktreader)
class PktreaderAdmin(ModelAdmin):
    pass
    # list_display = ("mac_addr", "ip_addr", "time")
    # list_filter = ('mac_addr', 'ip_addr')
    # search_fields = ('mac_addr', 'ip_addr')
