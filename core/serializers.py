 

from rest_framework.serializers import ModelSerializer

from core.models import RequestInfo


class RequestInfoSerializer(ModelSerializer):
    
    class Meta:
        model = RequestInfo
        fields = '__all__'