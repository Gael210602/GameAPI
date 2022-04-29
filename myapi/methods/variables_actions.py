from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import GameVariables
from myapi.serializers import VariablesSerializer

def variables_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        variables = VariablesSerializer(data=data)
        print(data)
        if variables.is_valid():
            variables.save()
            return JsonResponse(variables.data)
        else:
            return HttpResponse(status=400)
    elif request.method == 'GET':
        variables = GameVariables.objects.all()
        serializer = VariablesSerializer(variables, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(not_allowed(), status=405)