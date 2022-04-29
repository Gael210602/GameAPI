from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import Level
from myapi.serializers import LevelSerializer

def level_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        level = LevelSerializer(data=data)
        if level.is_valid():
            level.save()
            return JsonResponse(level.data)
        else:
            return HttpResponse(status=400)
    elif request.method == 'GET':
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(not_allowed(), status=405)