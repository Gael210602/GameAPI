from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import Attempt
from myapi.serializers import AttemptSerializer

def attempts_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        attempt = AttemptSerializer(data=data)
        if attempt.is_valid():
            attempt.save()
            return JsonResponse(attempt.data)
        else:
            return HttpResponse(status=400)
    elif request.method == 'GET':
        attempts = Attempt.objects.all()
        serializer = AttemptSerializer(attempts, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(not_allowed(), status=405)