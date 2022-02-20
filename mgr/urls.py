from django.urls import path
from mgr import customer, medicine
from mgr import sign_in_out

urlpatterns = [
    path('customers', customer.dispatcher),
    path('medicines', medicine.dispatcher),

    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]