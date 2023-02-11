from django.urls import path, include
from django_app.views.IndexView import StartPage
from django_app.views.GroupPage import GroupPage


urlpatterns = [
    path('', StartPage.as_view()),
    path('<uuid:schedule_group_id>/', GroupPage.as_view()),
]
