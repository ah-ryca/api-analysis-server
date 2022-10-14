from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..serializers.api_stat import APIStatSerializer, APIResult


class APIStatViewSet(ModelViewSet):
    def get_queryset(self):
        filters = self.request.GET
        api = filters.get('api')
        date_from = filters.get('from')
        date_to = filters.get('to')

        sql = f"""
                SELECT
                    1 as id,
                    created_at,
                    SUM(success) AS success,
                    SUM(fail) AS fail
                FROM
                    (
                        SELECT
                            created_at,
                            COUNT(success) AS success,
                            COUNT(fail) AS fail
                        FROM
                            (
                                SELECT
                                    DATE(request_time) as created_at,
                                    CASE
                                        WHEN status >= 200
                                        AND status < 300 THEN 200
                                    END AS success,
                                    CASE
                                        WHEN status < 200
                                        OR status >= 300 THEN 500
                                    END AS fail
                                FROM
                                    request_info
                                WHERE TRIM(request_path) LIKE '{api}%' AND request_time BETWEEN '{date_from}' AND '{date_to}'
                            ) AS t1
                        GROUP BY
                            created_at,
                            success,
                            fail
                    ) AS t2
                GROUP BY
                    created_at
                ORDER BY
                    created_at ASC;
        """

        return APIResult.objects.raw(sql)

    def list(self, request, *args, **kwargs):

        serializer = APIStatSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
