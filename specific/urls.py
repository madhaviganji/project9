from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('bhanu/',bhanu,name='bhanu'),
    path('kavitha/',kavitha,name='kavitha'),
]