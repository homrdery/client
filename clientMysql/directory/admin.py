from django.contrib.admin import ModelAdmin, register
from .models import *
@register(dirAddr)
class dirAddr(ModelAdmin):
    list_display = ("name", "mac_addr")
    search_fields = ('mac_addr', 'name')
    list_filter = ("mac_addr", )

# Register your models here.
