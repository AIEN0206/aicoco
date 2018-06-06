from django.urls import path, include
from . import views
app_name='portfolio'
urlpatterns = [
    path('', views.index,name='index'),
    path('select/', views.select, name='select'),
    path('detail/', views.detail, name='detail'),
    path('result/', views.result, name='result'),
    path('analyze/', views.analyze, name='analyze'),
    path('delete/', views.delete, name='delete')
]