from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun1),
    path('fun2/<d>',views.fun2),
    path('fun3',views.fun3.as_view()),
    path('fun4/<d>',views.fun4.as_view()),
    path('generic',views.genericapiview.as_view()),
    path('put_del/<id>',views.update.as_view())
    
]