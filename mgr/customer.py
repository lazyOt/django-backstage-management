import json
from django.http import JsonResponse

from mgr.views import listcustomers, addcustomer, modifycustomer, deletecustomer


from lib.handler import dispatcherBase
Action2Handler = {
    'list_customer': listcustomers,
    'add_customer': addcustomer,
    'modify_customer': modifycustomer,
    'del_customer': deletecustomer,
}

def dispatcher(request):
    return dispatcherBase(request, Action2Handler)
