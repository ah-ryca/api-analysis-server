from django.db import models

__all__ = 'Browser', 'OS', 'DeviceInfo'

from .helper import TYPE
from .request_info import RequestInfo


class Browser(models.Model):
    request = models.OneToOneField(RequestInfo, on_delete=models.CASCADE, related_name='browser')
    family = models.CharField(max_length=50, null=True)
    version = models.CharField(max_length=50, null=True)
    version_string = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'device_browser'


class OS(models.Model):
    request = models.OneToOneField(RequestInfo, on_delete=models.CASCADE, related_name='os')
    family = models.CharField(max_length=50, null=True)
    version = models.CharField(max_length=50, null=True)
    version_string = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'device_os'


class DeviceInfo(models.Model):
    request = models.OneToOneField(RequestInfo, on_delete=models.CASCADE, related_name='device_info')
    brand = models.CharField(max_length=50, null=True)
    family = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    device_type = models.SmallIntegerField(default=TYPE.OTHER, choices=TYPE.choices)

    class Meta:
        db_table = 'device_info'
