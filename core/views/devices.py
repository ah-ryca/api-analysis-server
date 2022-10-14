from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import RequestInfo
from ..serializers.devices import DevicesInfoSerializer


class DevicesViewSet(ModelViewSet):
    serializer_class = DevicesInfoSerializer

    def get_queryset(self):
        filters = self.request.GET

        date_from = filters.get('from')
        date_to = filters.get('to')
        sql = f"""
                SELECT
                    1 AS id,
                    http_user_agent AS user_agent,
                    COUNT(http_user_agent) AS count
                FROM
                    request_info
                --WHERE
                --    request_time >= {date_from}
                --    AND request_time <= {date_to}
                GROUP BY
                    http_user_agent
        """
        return RequestInfo.objects.raw(sql)

    def get_devices(self, request, *args, **kwargs):
        serializer = DevicesInfoSerializer(data=self.get_queryset(), many=False)
        return Response(serializer.data)
