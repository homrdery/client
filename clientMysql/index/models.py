from django.db import models

class PktRecordLog(models.Model):
    type = models.IntegerField("Тип", null=False, help_text="Тип записи")
    data = models.JSONField("Данные", null=False, help_text="Данные пакета")
    time = models.DateTimeField("Время", null=False, help_text="Время добавления")
    def __str__(self):
        return f"пакет ({self.id}) {self.data}:{self.time}"
    class Meta:
        verbose_name = "пакет"
        verbose_name_plural = "пакеты"


class Pktreader(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, blank=False, primary_key=True, help_text="mac адрес pc")
    ip_addr = models.CharField("ip_addr", max_length=32, null=False, blank=False, help_text="ip адрес pc")
    time = models.DateTimeField("time", null=False, help_text="Время обнуружения pc")
    def __str__(self):
        return f"компьютер {self.mac_addr}:{self.ip_addr}:{self.time}"
    class Meta:
        verbose_name = "компьютер"
        verbose_name_plural = "компьютеры"

class worker(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, blank=False, primary_key=True, help_text="mac адрес pc")
    name = models.CharField("name", max_length=30, null=False, blank=False, help_text="фио работника")
    time = models.DateTimeField("Время", null=False, help_text="Время добавления")
    def __str__(self):
        return f"Работник {self.mac_addr}:{self.name}:{self.time}"
    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"