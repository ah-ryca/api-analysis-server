from django.urls import path 
from .views import RequestInfoViewSet
urlpatterns = [
    path('v1/requests', RequestInfoViewSet.as_view({'get': 'list'}), name='requests'),
]