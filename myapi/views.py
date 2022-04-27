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
