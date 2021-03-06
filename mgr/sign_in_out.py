from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout


# 处理登录
def signin(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    user = authenticate(username=userName, password=passWord)

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账号登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '该用户已被禁用'})
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


# 处理登出
def signout(request):
    logout(request)
    return JsonResponse({'ret': 0})