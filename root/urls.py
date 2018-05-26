from django.urls import path
from . import views

app_name = "root"

urlpatterns = [
    path('', views.index, name="index"),
    path('__empty/', views.empty, name="__empty"),
]
