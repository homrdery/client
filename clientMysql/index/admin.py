from django.contrib.admin import ModelAdmin, register
from .models import *

@register(PktRecordLog)
class PktRecordLogAdmin(ModelAdmin):
    pass


@register(Pktreader)
class PktreaderAdmin(ModelAdmin):
    pass
