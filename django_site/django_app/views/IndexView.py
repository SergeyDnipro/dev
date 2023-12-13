from django_app.models.ScheduleRecord import Record
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django_app.task.msg_to_telegram import msg_to_telegram
from django.forms import modelformset_factory, formset_factory
from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import DeleteView
from django.db import IntegrityError
from django.urls import reverse_lazy


class StartPage(TemplateView):
    template_name = 'django_app/index2.html'

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.result = None
    #     self.msg = ''
    #
    # def get(self, request, *args, **kwargs):
    #     self.result = Record.objects.all().order_by('holder__username')
    #     for element in self.result:
    #         if element.status == Record.Status.COMPLETED:
    #             self.msg += f"Completed task - {element.created.strftime('%Y-%b-%d - %H:%m')} {element.holder} {element.description}\n"
    #     msg_to_telegram(self.msg)
    #     return super(StartPage, self).get(self)

    def get_context_data(self, **kwargs):
        result = Record.objects.all().order_by('holder__username')
        users = User.objects.all()
        return {'items': result, 'users': users}


class ConfirmDelete(DeleteView):
    template_name = 'django_app/multi_delete_confirm.html'
    model = Record
    success_url = reverse_lazy('start_page')
    delete_list = []

    def get(self, request, *args, **kwargs):
        print(self.request.POST)
        return super(ConfirmDelete, self).get(self, *args, **kwargs)

    def get_queryset(self):
        queryset = super(ConfirmDelete, self).get_queryset()
        self.queryset = queryset.filter(id__in=self.delete_list)
        return self.queryset

    def get_object(self, queryset=None):
        return self.get_queryset()

    def post(self, request, *args, **kwargs):
        self.delete_list = self.request.POST.getlist('delete_list')
        print(self.delete_list)
        if self.request.POST.get('confirm_delete'):
            result = self.get_queryset()
            print(result)
            result.delete()
            return redirect(reverse('start_page'))
        return self.get(self, *args, **kwargs)


def formset_view(request):
    users = User.objects.all()
    changed_records = []
    formset = modelformset_factory(
        Record,
        fields=['id', 'holder', 'schedule_group', 'description', 'status'],
        can_delete=True,
        extra=0
    )
    # if 'delete' in request.POST:
    #     print(request.POST)
    if request.method == 'POST':
        formview = formset(request.POST)
        print(formview)
        if formview.is_valid():
            # print(formview)
            if 'delete' in request.POST:
                for el in formview.deleted_objects:
                    print(el)
                    el.delete()
                return redirect('start_page')
            formview.save(commit=False)
            deleted_records = formview.deleted_objects
            for element in formview.changed_objects:
                changed_records.append(element[0])
            # print(deleted_records)
            # print(changed_records)
            # print(formview.changed_objects)
            return render(request, 'django_app/index1.html', {"items": deleted_records, "items1": changed_records})
    formview = formset()
    return render(request, 'django_app/index.html', {"items": formview, 'users': users})


def confirm_delete(request, **kwargs):
    formview = kwargs['form']
    deleted_view = kwargs['form'].deleted_objects
    if request.method == 'POST':
        formview.save()
        return redirect('start_page')
    else:
        return render(request, 'django_app/index.html', {"items": deleted_view})


class BulkEditView(DeleteView):

    def get(self, request, *args, **kwargs):
        try:
            self.queryset = Record.objects.filter(**kwargs)
        except IntegrityError:
            self.queryset = Record.objects.all()
        result = self.queryset
        users = User.objects.all()
        return render(request, 'django_app/index.html', {'items': result, 'users': users})

    def post(self, request, *args, **kwargs):
        pass
