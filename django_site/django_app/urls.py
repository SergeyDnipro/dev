from django.urls import path, include
from django_app.views.IndexView import StartPage, ConfirmDelete
from django_app.views.GroupPage import GroupPage, SinglePage
from django_app.views.CreateRecordView import SingleRecordCreateView, SingleRecordUpdateView, edit_record_view
from django_app.views.DeleteRecordView import DeleteRecordView
from django_app.views.IndexView import formset_view, confirm_delete, BulkEditView


urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('test_delete/', ConfirmDelete.as_view(), name='confirm_delete'),
    path('users/<str:holder__username>/', GroupPage.as_view(), name='user_page'),
    path('records/<uuid:id>/', edit_record_view, name='element_page'),
    path('add/', SingleRecordCreateView.as_view(), name='add_record'),
    path('delete/<pk>/', DeleteRecordView.as_view(), name='delete_record'),
]
