from django.db import models

class PktRecordLog(models.Model):
    type = models.IntegerField("type", null=False, help_text="Тип записи")
    data = models.JSONField("data", null=False, help_text="Данные пакета")
    time = models.DateTimeField("time", null=False, help_text="Время добавления")
    class Meta:
        verbose_name = "пакет"
        verbose_name_plural = "пакеты"


class Pktreader(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, blank=False, help_text="mac адрес pc")
    ip_addr = models.CharField("id_addr", max_length=32, null=False, blank=False, help_text="ip адрес pc")
    time = models.DateTimeField("time", null=False, help_text="Время обнуружения pc")
    class Meta:
        verbose_name = "компьютор"
        verbose_name_plural = "компьюторы"