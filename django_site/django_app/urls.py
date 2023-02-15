from django.urls import path, include
from django_app.views.IndexView import StartPage
from django_app.views.GroupPage import GroupPage, SinglePage
from django_app.views.CreateRecordView import SingleRecordCreateView


urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('users/<str:holder__username>/', GroupPage.as_view(), name='user_page'),
    path('records/<uuid:id>/', SinglePage.as_view(), name='element_page'),
    path('add/', SingleRecordCreateView.as_view(), name='add_record'),
]
