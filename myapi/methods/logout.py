from django.http import HttpResponse, JsonResponse
from gameapi.constants import encrypt_key
from rest_framework.parsers import JSONParser
from myapi.models import User
from myapi.serializers import SessionSerializer, UserSerializer
import jwt
from datetime import datetime

def logout_method(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        encoded_jwt = data['jwt']
        try:
            decoded_jwt = jwt.decode(encoded_jwt, encrypt_key(), algorithms=["HS256"])
            user_obj = User.objects.get(email=decoded_jwt['email'])
        except User.DoesNotExist:
            return HttpResponse(status=404)
        print(decoded_jwt)
        now = datetime.now()
        
        user = UserSerializer(user_obj)

        data = {
            'sign_in': decoded_jwt['sign_in'],
            'sign_out': str(now),
            'user_id': user.data['user_id'],
            'jwt': encoded_jwt
        }

        serializer = SessionSerializer(data = data )

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
        
    else:
        return JsonResponse(status=405)
