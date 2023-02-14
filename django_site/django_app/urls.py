from django.urls import path, include
from django_app.views.IndexView import StartPage
from django_app.views.GroupPage import GroupPage, SinglePage


urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('<str:holder__username>/', GroupPage.as_view(), name='user_page'),
    path('<str:holder__username>/<uuid:id>/', SinglePage.as_view(), name='element_page'),
]
