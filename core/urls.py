from django.urls import path

from core.views.api_stat import APIStatViewSet
from core.views.charge_account import get_charge_account_info
from core.views.devices import DevicesViewSet
from core.views.request_info import RequestInfoViewSet

from core.views.app_pages import AppPageViewSet

urlpatterns = [
    path('v1/requests', RequestInfoViewSet.as_view({'get': 'list'}), name='requests'),

    path('v1/app/pages', AppPageViewSet.as_view({'get': 'list'}), name='list_of_pages'),
    path('v1/app/page/<int:page_id>', AppPageViewSet.as_view({'get': 'get_page_detail'}), name='page_detail'),

    path('v1/api-stat', APIStatViewSet.as_view({'get': 'list'}), name='api_stat'),

    path('v1/device/info', DevicesViewSet.as_view({'get': 'get_devices'}), name='devices'),
    path('v1/os/info', DevicesViewSet.as_view({'get': 'get_os'}), name='os'),
    path('v1/browser/info', DevicesViewSet.as_view({'get': 'get_browser'}), name='browser'),

    # Charge
    path('v1/charge-account',
         get_charge_account_info
         , name='charge_account'),
]
