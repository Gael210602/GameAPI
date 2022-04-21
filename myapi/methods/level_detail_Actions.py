from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import Level
from myapi.serializers import LevelSerializer

def single_level_actions(request, pk):
    try:
        level_obj = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LevelSerializer(level_obj)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LevelSerializer(level_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        level_obj.delete()
        return HttpResponse(status=204)
    else:
        return JsonResponse(not_allowed(), status=405)