from django.http import JsonResponse
from django.db.models import F
from django.db import IntegrityError, transaction

from common.models import Order,OrderMedicine
import json

from lib.handler import dispatcherBase

# -----处理多对多请求
def addorder(request):
    info = request.params['data']

    with transaction.atomic():
        new_order = Order.objects.create(name=info['name'],
                                       customer_id=info['customerid'])
        batch = [OrderMedicine(order_id=new_order.id,medicine_id=mid,amount=1)
               for mid in info['medicineids']]

        OrderMedicine.objects.bulk_create(batch)
    return JsonResponse({'ret': 0, 'id': new_order.id})

def listorder(request):
    # 返回一个QuerySet对象，包含所有表的记录
    qs = Order.objects\
        .annotate(
            # ---重命名
            customer_name=F('customer__name'),
            medicines_name=F('medicines__name')
        )\
        .values('id','name','create_date',
                              # 两个下划线，表示取customer外键关联的表中的name字段的值
                              'customer__name',
                              'medicines_name'
                        )
    retlist = list(qs)

    #----可能有ID相同，药品不同的订单记录，需要合并
    newlist = []
    id2order = {}
    for one in retlist:
        orderid = one['id']
        if orderid not in id2order:
            newlist.append(one)
            id2order[orderid] = one
        else:
            id2order[orderid]['medicines_name'] += '|' + one['medicines_name']

    return JsonResponse({'ret': 0, 'retlist': newlist})


Action2Handler = {
    'list_order': listorder,
    'add_order': addorder
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)

