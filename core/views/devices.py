from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import RequestInfo
from ..serializers.devices import DevicesInfoSerializer


class DevicesViewSet(ModelViewSet):
    serializer_class = DevicesInfoSerializer

    def get_filters(self):
        filters = self.request.GET

        date_from = filters.get('from')
        date_to = filters.get('to')

        return date_from, date_to

    def get_queryset(self):
        date_from, date_to = self.get_filters()
        sql = f"""
                SELECT
                    1 AS id,
                    http_user_agent AS user_agent,
                    COUNT(http_user_agent) AS count
                FROM
                    request_info
                WHERE
                    request_time BETWEEN '{date_from}' AND '{date_to}'
                GROUP BY
                    http_user_agent
        """
        return RequestInfo.objects.raw(sql)

    # def get_devices(self, request, *args, **kwargs):
    #     serializer = DevicesInfoSerializer(data=self.get_queryset(), many=False)
    #     return Response(serializer.data)
    def get_devices(self, request, *args, **kwargs):
        date_from, date_to = self.get_filters()
        from core.models import DeviceInfo
        sql = f"""
        select 1 as id, 
         device_type,
         count
         FROM 
       (     select 
            CASE
                when device_type=1 then 'موبایل' 
                when device_type=2 then 'تبلت' 
                when device_type=3 then 'کامپیوتر' 
                when device_type=4 then 'touchable' 
                when device_type=5 then 'بات' 
                when device_type=6 then 'ناشناس' 
            end as device_type,
             count(device_type) over (partition by device_type) as count 
             from device_info 
             inner join request_info on request_id = request_info.id
                             WHERE
                    request_info.request_time BETWEEN '{date_from}' AND '{date_to}'
             ) as t1
        group by device_type, count
        """
        device_info = DeviceInfo.objects.raw(sql)
        output = []
        for device in device_info:
            tmp = {'name': device.device_type, 'count': device.count}
            output.append(tmp)

        return Response(output)

    def get_os(self, request, *args, **kwargs):
        date_from, date_to = self.get_filters()
        from core.models import OS

        sql = f"""
         select 1 as id,     
         family, 
         count
       from
           (   select family,
              count(family) over (partition by family) as count
              from device_os
              inner join request_info on request_id = request_info.id
                              WHERE
                     request_info.request_time BETWEEN '{date_from}' AND '{date_to}') as t1

         group by family, count
         """

        device_info = OS.objects.raw(sql)
        output = []
        for device in device_info:
            tmp = {'name': device.family, 'count': device.count}
            output.append(tmp)

        return Response(output)

    def get_browser(self, request, *args, **kwargs):
        date_from, date_to = self.get_filters()
        from core.models import OS

        sql = f"""
         select 1 as id,     
         family, 
         count
       from
           (   select family,
              count(family) over (partition by family) as count
              from device_browser
              inner join request_info on request_id = request_info.id
                              WHERE
                     request_info.request_time BETWEEN '{date_from}' AND '{date_to}') as t1

         group by family, count
         """

        device_info = OS.objects.raw(sql)
        output = []
        for device in device_info:
            tmp = {'name': device.family, 'count': device.count}
            output.append(tmp)

        return Response(output)
