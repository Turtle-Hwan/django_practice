from django.urls import path

from . import views

urlpatterns = [
    path('name/', views.index, name='myname'),
    path('', views.mainPage, name='main'),

]