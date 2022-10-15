from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_charge_account_info(request):
    filters = request.GET
    from requests import get
    result = get('http://localhost:8077/api/v1/_statistics', params=filters)
    from rest_framework.response import Response
    return Response(data=result.json())
