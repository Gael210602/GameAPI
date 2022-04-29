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
    h_var = 'Country'
    v_var = 'Popularity'
    data = [[h_var,v_var]]

    h_var_json = dumps(h_var)
    v_var_json = dumps(v_var)

    mydb = sqlite3.connect("db.sqlite3")
    cur = mydb.cursor()
    stringSQL = ''' SELECT DISTINCT country FROM myapi_user '''
    rows = cur.execute(stringSQL)

    for i in rows:
        r = {}
        r['country'] = i[0]

        data.append([i[0],""])
    datos_json = dumps(data)
    
    return render(request, 'grafica.html', {'values':datos_json,'h_title':h_var_json,'v_title':v_var_json})