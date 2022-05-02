from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import SessionData
from myapi.serializers import SessionDataSerializer

def sesion_data_methods(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        session_sata = SessionDataSerializer(data=data)
        if session_sata.is_valid():
            session_sata.save()
            return JsonResponse(session_sata.data)
        else:
            return JsonResponse({'message':'Por favor elija otro nombre de usuario y verifique su correo'}, status=204)
    elif request.method == 'GET':
        session_data = SessionData.objects.all()
        serializer = SessionDataSerializer(session_data, many=True)
        return JsonResponse(serializer.data, safe=False)
