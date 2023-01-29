from django.urls import path, include
from django_app.views.test_view import index


urlpatterns = [
    path('', index),
]