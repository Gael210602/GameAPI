from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import Attempt
from myapi.serializers import AttemptSerializer

def single_user_actions(request, pk):
    try:
        attempt_obj = Attempt.objects.get(pk=pk)
    except Attempt.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AttemptSerializer(attempt_obj)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AttemptSerializer(attempt_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        attempt_obj.delete()
        return HttpResponse(status=204)
    else:
        return JsonResponse(not_allowed(), status=405)