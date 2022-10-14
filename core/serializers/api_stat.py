from django.db import models
from rest_framework.serializers import ModelSerializer


class APIResult(models.Model):
    success = models.IntegerField(default=0)
    fail = models.IntegerField(default=0)
    created_at = models.DateField()


class APIStatSerializer(ModelSerializer):
    class Meta:
        model = APIResult
        fields = '__all__'
