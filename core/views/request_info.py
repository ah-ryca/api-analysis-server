from rest_framework.viewsets import ModelViewSet

from ..models import RequestInfo
from ..helper.pagination import Pagination
from ..serializers.request_info import RequestInfoSerializer


class RequestInfoViewSet(ModelViewSet):
    queryset = RequestInfo.objects.all().order_by('-id')
    serializer_class = RequestInfoSerializer
    pagination_class = Pagination
