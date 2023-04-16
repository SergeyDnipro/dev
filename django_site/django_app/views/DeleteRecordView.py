from django.views.generic.edit import DeleteView
from django_app.forms.SingleRecordForm import SingleRecordForm, SingleEditRecordForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django_app.models.ScheduleRecord import Record
from django.shortcuts import render, redirect, get_object_or_404, reverse


class DeleteRecordView(DeleteView):
    model = Record
    success_url = reverse_lazy('start_page')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.holder:
            return render(request, 'django_app/record_restrict_delete.html', {'object': self.object})
        return super().get(self)
