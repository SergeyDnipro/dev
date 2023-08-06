from django.views.generic.edit import DeleteView
from django_app.forms.SingleRecordForm import SingleRecordForm, SingleEditRecordForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django_app.models.ScheduleRecord import Record
from django.shortcuts import render, redirect, get_object_or_404, reverse


class DeleteRecordView(DeleteView):
    model = Record
    success_url = reverse_lazy('start_page')

    def get_queryset(self):
        self.queryset = Record.objects.all()
        return self.queryset

    def get_object(self, queryset=None):
        return self.get_queryset()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        if self.request.user != self.object[0].holder:
            return render(request, 'django_app/record_restrict_delete.html', {'object': self.object})
        return super().get(self)

    def post(self, request, *args, **kwargs):
        self.items_to_del = self.request.POST.getlist('is_checked')
        print(self.items_to_del)
        return self.get(self, *args, **kwargs)

