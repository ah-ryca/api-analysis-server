from rest_framework.serializers import ModelSerializer

from core.models import Page


class PageListSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'name',)
