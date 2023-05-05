from django.urls import path
from .views import *
app_name = 'pay'

urlpatterns = [
    path('',CreateClickTransactionView.as_view()),
    path('click/transection',ClickTransactionTestView.as_view()),
]