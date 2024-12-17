from django.urls import path
from .views import *

urlpatterns=[
    path('maintanceList',ModeloView.as_view(),name="maintance"),
    path('',HomeviewMaintance.as_view(),name="homeMaintance"),
]