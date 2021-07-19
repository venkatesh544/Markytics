from django.urls import path

from Mark1 import views


app_name='Mark1'

urlpatterns = [
    path('',views.home),
    path('introducation', views.Introducation,name='introducation'),
    path('deatils', views.Deatils, name='deatils'),
    path('loginpage', views.Loginpage, name='loginpage'),
    path('registeration', views.Registeration, name='registeration'),
    path('save', views.Save, name='save'),
    path('sent', views.Sent, name='sent'),
    path('other', views.Other, name='other'),
    path('logged', views.Logged, name='logged'),
    path('loginout', views.Loginout, name='loginout'),

]