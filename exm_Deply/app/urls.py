from django.urls import path
from .views import *

urlpatterns=[
    path('maintanceList',ModeloView.as_view(),name="maintancevw"),
    path('',HomeBascosta.as_view(),name="HomeBascosta"),
]