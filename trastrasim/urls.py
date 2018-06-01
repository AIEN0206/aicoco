from django.urls import path
from . import views

app_name='trastrasim'
urlpatterns = [
    path('', views.index,name='index'),
    path('compinfo/', views.company_info,name='companyinfo'),
    path('sc/<int:id>', views.strategy_choice,name='strategychoice'),     
    path('du/', views.stocks_price_update,name='dailyupdate'),
    path('cu/', views.company_info_update,name='companyupdate'),
]