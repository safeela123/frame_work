"""
URL configuration for one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from one_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi',views.fun1),
    path('data',views.fun2),
    path('data/<name>',views.fun3),
    path('hlo/<int:age>',views.fun4),
    path('hlo/<int:a>/<int:b>/<int:c>',views.fun5),
    path('',views.fun6),
    path('hey/<c>',views.fun7),
    path('fun8',views.fun8),
    path('fun9',views.fun9),
    path('fun10',views.fun10)
]
