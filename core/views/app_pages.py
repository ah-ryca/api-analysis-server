from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Page
from core.serializers.api_stat import APIResult, APIStatSerializer
from core.serializers.app_pages import PageListSerializer


class AppPageViewSet(ModelViewSet):
    queryset = Page.objects.all().order_by('-id')
    serializer_class = PageListSerializer

    def get_page_detail(self, request, *args, **kwargs):
        page_id = kwargs.get('page_id')

        apis = [f"TRIM(request_path) LIKE  '%{path}%'" for path in
                Page.objects.get(pk=page_id).apis.values_list('path', flat=True)]
        api_conditions = ' OR '.join(apis)

        filters = self.request.GET
        date_from = filters.get('from')
        date_to = filters.get('to')

        sql = f"""
                SELECT
                    1 as id,
                    created_at,
                    SUM(success)/{len(apis)} AS success
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
                                WHERE {api_conditions} AND request_time BETWEEN '{date_from}' AND '{date_to}'
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
        queryset = APIResult.objects.raw(sql)
        serializer = APIStatSerializer(queryset, many=True)
        return Response(serializer.data)
