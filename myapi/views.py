from re import template
from django.views.decorators.csrf import csrf_exempt
from myapi.methods.attempt_action import attempt_actions
from myapi.methods.attempts_actions import attempts_actions
from myapi.methods.level_detail_Actions import single_level_actions
from myapi.methods.levels_list import level_actions
from myapi.methods.login import loginmethod
from myapi.methods.logout import logout_method
from myapi.methods.session_list import session_list_actions
from myapi.methods.single_user_actions import single_user_actions
from myapi.methods.userActions import user_actions
from myapi.methods.user_variable_actions import user_variable_get
from myapi.methods.variables_actions import variables_actions
from json import dumps, loads
import sqlite3
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

from myapi.models import Attempt, GameVariables
from myapi.serializers import AttemptSerializer, VariablesSerializer


@csrf_exempt
def user_list(request):
    return user_actions(request=request)


@csrf_exempt
def user_detail(request, pk):
    return single_user_actions(request, pk)


@csrf_exempt
def login(request):
    return loginmethod(request=request)


@csrf_exempt
def logout(request):
    return logout_method(request=request)


@csrf_exempt
def session_list(request):
    return session_list_actions(request=request)


@csrf_exempt
def levels_list(request):
    return level_actions(request=request)


@csrf_exempt
def level_detail(request, pk):
    return single_level_actions(request, pk)


@csrf_exempt
def attempt_list(request):
    return attempts_actions(request)


@csrf_exempt
def attempt_detail(request, pk):
    return attempt_actions(request, pk)


@csrf_exempt
def variables_list(request):
    return variables_actions(request)


@csrf_exempt
def single_variables_user(request, pk):
    return user_variable_get(request, pk)


@csrf_exempt
def grafica(request):

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

    return render(request, 'grafica.html', {'lvl1_win': lvl1_win, 'lvl2_win': lvl2_win, 'lvl3_win': lvl3_win, 'lvl1_lost': lvl1_lost, 'lvl2_lost': lvl2_lost, 'lvl3_lost': lvl3_lost})
