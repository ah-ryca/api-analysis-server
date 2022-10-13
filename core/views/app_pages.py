from rest_framework.viewsets import ModelViewSet

from core.models import Page
from core.serializers.app_pages import PageListSerializer


class AppPageViewSet(ModelViewSet):
    queryset = Page.objects.all().order_by('-id')
    serializer_class = PageListSerializer
