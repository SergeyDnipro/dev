from django.views.generic.edit import DeleteView
from django_app.forms.SingleRecordForm import SingleRecordForm, SingleEditRecordForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django_app.models.ScheduleRecord import Record
from django.shortcuts import render, redirect, get_object_or_404


class DeleteRecordView(DeleteView):
    model = Record
    success_url = reverse_lazy('start_page')
