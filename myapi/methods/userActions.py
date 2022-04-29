from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import User
from myapi.serializers import UserSerializer

def user_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = UserSerializer(data=data)
        if user.is_valid():
            user.save()
            return JsonResponse(user.data)
        else:
            return JsonResponse({'message':'Por favor elija otro nombre de usuario y verifique su correo'}, status=204)
    elif request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)