from django.urls import path
from .import views
urlpatterns=[
    path('fun3',views.fun3),
    path('fun4/<d>',views.fun4)
]