"""
URL configuration for sample project.

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
from app import views     # here have to import our app and view file here

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.fun1),  # here first '' is called path..we can make it empty and we can write there.
    # path('hai',views.fun2), # can't name multiple paths same name ie hai to both paths for fun1 and fun2
    #                          # here have to add ' /hai ' to url entrypanel in browser to get fun2
    # path('hey/<name>',views.fun3),  # in output if you give /hey manu then it displays fun3manu . if u give 
    #                                 # give /hey/hary then it displays fun3hari
    # path('hello/<int:age>',views.fun4),  # these have to run in project file ie sample file eg:work\framework\sample>
    # path('largest/<int:a>/<int:b>/<int:c>',views.fun5),
    # path('',views.fun6),
    # path('data/<c>',views.fun7),
    # path('data',views.fun8)
    # path('data',views.fun9),
    path('data',views.fun10),
    # path('data',views.ele_city)
    
]