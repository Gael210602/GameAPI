from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import GameVariables
from myapi.serializers import VariablesSerializer

def user_variable_get(request, pk):
    try:
        game_var = GameVariables.objects.get(user_id=pk)
    except GameVariables.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VariablesSerializer(game_var)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VariablesSerializer(game_var, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        game_var.delete()
        return HttpResponse(status=204)
    else:
        return JsonResponse(not_allowed(), status=405)