from django.db import models
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from user_agents import parse


class Devices(models.Model):
    user_agent = models.CharField(max_length=300)
    count = models.IntegerField()


class DevicesInfoSerializer(ModelSerializer):
    user_agent = SerializerMethodField()
    agent = SerializerMethodField()

    class Meta:
        model = Devices
        fields = '__all__'

    def get_user_agent(self, instance):
        return str(parse(instance.user_agent))

    def get_agent(self, instance):
        return instance.user_agent
