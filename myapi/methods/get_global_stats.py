

from django.http import HttpResponse, JsonResponse
from gameapi.constants import not_allowed
from rest_framework.parsers import JSONParser
from myapi.models import User
from myapi.serializers import AttemptSerializer, UserSerializer

def get_global_stats(request):
    if request.method == 'GET':
        variables = Attempt.objects.all()
        serializer = AttemptSerializer(variables, many=True)
        print(serializer.data)
        lvl1_lost = 0
        lvl2_lost = 0
        lvl3_lost = 0

        lvl1_win = 0
        lvl2_win = 0
        lvl3_win = 0

        for element in serializer.data:
            if element['level_id'] == 7 and element['status'] == True:
                lvl1_win = lvl1_win + 1
            if element['level_id'] == 8 and element['status'] == True:
                lvl2_win = lvl2_win + 1
            if element['level_id'] == 9 and element['status'] == True:
                lvl3_win = lvl3_win + 1

            if element['level_id'] == 7 and element['status'] == False:
                lvl1_lost = lvl1_lost + 1
            if element['level_id'] == 8 and element['status'] == False:
                lvl2_lost = lvl2_lost + 1
            if element['level_id'] == 9 and element['status'] == False:
                lvl3_lost = lvl3_lost + 1

        response = {
            'lvl1_lost':lvl1_lost,
            'lvl2_lost': lvl2_lost,
            'lvl3_lost': lvl3_lost,
            'lvl1_win': lvl1_win,
            'lvl2_win': lvl2_win,
            'lvl3_win': lvl3_win
        }
        return JsonResponse(response, safe=False)
    else:
        return JsonResponse(not_allowed(), status=405)