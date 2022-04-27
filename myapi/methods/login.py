from django.http import HttpResponse, JsonResponse
from gameapi.constants import encrypt_key
from rest_framework.parsers import JSONParser
from myapi.models import User
from myapi.serializers import UserSerializer
import bcrypt
import jwt
from datetime import datetime

login_error = {'message':'Invalid credentials'}

def loginmethod(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_name = data['user_name']
        password = data['password'].encode("utf-8")
        try:
            user_obj = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            return HttpResponse(status=404)
            
        user = UserSerializer(user_obj)

        if bcrypt.checkpw(password, user.data['password'].encode("utf-8")):
            now = datetime.now()
            encoded_jwt = jwt.encode({"user_name": user.data['user_name'], 'sign_in': str(now), 'email':user.data['email'] }, encrypt_key(), algorithm="HS256")
            print("User: "+user.data['user_name']+' logged at: '+ str(now)) 
            return JsonResponse({'message':'Login successful', 'jwt': encoded_jwt, 'user_id': user.data['user_id']}, status=201)
        return JsonResponse(login_error, status=401)
        
    else:
        return JsonResponse(status=405)