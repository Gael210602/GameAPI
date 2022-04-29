from django.http import JsonResponse
from gameapi.constants import not_allowed
from myapi.models import Session
from myapi.serializers import SessionSerializer

def session_list_actions(request):
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse(not_allowed(), status=405)
