from django.db import models
from django.utils import timezone

class HotspotSession(models.Model):
    ssid = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return f"Hotspot Session (SSID: {self.ssid})"

    def stop(self):
        self.end_time = timezone.now()
        self.is_active = False
        self.save()