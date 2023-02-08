from django.urls import path, include
from django_app.views.IndexView import StartPage


urlpatterns = [
    path('', StartPage.as_view()),
]
