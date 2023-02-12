from django.urls import path, include
from django_app.views.IndexView import StartPage
from django_app.views.GroupPage import GroupPage


urlpatterns = [
    path('', StartPage.as_view()),
    path('<str:holder__username>/', GroupPage.as_view()),
]
