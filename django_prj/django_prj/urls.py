"""hillel_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from todo import views
from todo.views import ToDoOutDateID, ToDoOutAll, OneItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/done/', views.todo_out_done),
    re_path(r'^|^todo/$', OneItemView.as_view()),
    re_path(r'^todo/(?P<name>[a-zA-Z\s]{0,50})/$|^todo/(?P<group__date>[0-9]{4}.[0-9]{2}.[0-9]{2})/$|'
            '^todo/(?P<id>[0-9]{0,4})/$', ToDoOutDateID.as_view()),
]
