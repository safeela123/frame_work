from django.urls import path
from .import views

urlpatterns =[
    path('register',views.userReg),
    path('',views.userlogin),
    path('index',views.index),
    path('logout',views.logout)
]