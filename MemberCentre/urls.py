from django.urls import path,include
from MemberCentre import views
app_name='MemberCentre'
urlpatterns = [
    #http://localhost:8000/index/
    path('index/<str:account>', views.index,name='index'),
    path('index_delete/<str:account>', views.index_delete,name='index_delete'),
    path('create/', views.create,name='create'),
    path('space/<str:account>', views.space,name='space'),
    path('update/<str:account>', views.update,name='update'),
    path('delete/<str:account>', views.delete,name='delete'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('forget/', views.forget,name='forget'),
    path('grade/', views.grade,name='grade'),
    path('grade_forget/', views.grade_forget,name='grade_forget'),
] 