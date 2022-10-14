from django.urls import path

from core.views.api_stat import APIStatViewSet
from core.views.request_info import RequestInfoViewSet

from core.views.app_pages import AppPageViewSet

urlpatterns = [
    path('v1/requests', RequestInfoViewSet.as_view({'get': 'list'}), name='requests'),
    path('v1/app/pages', AppPageViewSet.as_view({'get': 'list'}), name='list_of_pages'),
    path('v1/api-stat/<str:path>', APIStatViewSet.as_view({'get': 'list'}), name='list_of_pages'),
]
