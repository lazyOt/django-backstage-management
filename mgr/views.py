from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from common.models import Customer


def listcustomers(request):
    qs = Customer.objects.values()
    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


def addcustomer(request):
    info = request.params['data']

    record = Customer.objects.create(name=info['name'],
                                     phonenumber=info['phonenumber'],
                                     address=info['address'])
    return JsonResponse({'ret': 0, 'id': record.id})

def modifycustomer(request):
    # 从请求消息中，获取修改客户的信息
    # 找到该客户 操作
    customerid = request.params['id']
    newdata = request.params['newdata']

    try:
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{customerid}`的客户不存在'
        }
    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.address = newdata['address']

    customer.save()
    return JsonResponse({'ret': 0})

def deletecustomer(request):
    customerid = request.params['id']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    customer.delete()
    return JsonResponse({'ret': 0})