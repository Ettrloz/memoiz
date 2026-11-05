from django.urls import path
from . import views

app_name = 'memoiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('memo/<int:memo_id>/', views.detail, name='detail'),
]