from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import User
from myapi.serializers import UserSerializer

def single_user_actions(request, pk):
    try:
        user_objs = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user_objs)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user_objs, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user_objs.delete()
        return HttpResponse(status=204)
    else:
        return JsonResponse(not_allowed(), status=405)