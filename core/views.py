from django.db.models import Q
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import RequestInfo
from .helper.pagination import Pagination
from .serializers import RequestInfoSerializer

class RequestInfoViewSet(viewsets.ModelViewSet):
    queryset = RequestInfo.objects.all().order_by('-id')
    serializer_class = RequestInfoSerializer
    pagination_class = Pagination