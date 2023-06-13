from django_app.models.ScheduleRecord import Record
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django_app.task.msg_to_telegram import msg_to_telegram
from django.forms import modelformset_factory, formset_factory
from django.shortcuts import render, redirect, reverse


class StartPage(TemplateView):
    template_name = 'django_app/index.html'

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


def formset_view(request):
    changed_records = []
    formset = modelformset_factory(Record, fields=['id', 'holder', 'schedule_group', 'description', 'status'], can_delete=True)
    if 'delete' in request.POST:
        print(request.POST)
    if request.method == 'POST':
        formview = formset(request.POST)
        if formview.is_valid():
            if 'delete' in request.POST:
                for el in formview.deleted_objects:
                    print(el)
                    el.delete()
                return redirect('start_page')
            formview.save(commit=False)
            deleted_records = formview.deleted_objects
            for element in formview.changed_objects:
                changed_records.append(element[0])
            print(deleted_records)
            return render(request, 'django_app/index1.html', {"items": deleted_records, "items1": changed_records})
    formview = formset()
    return render(request, 'django_app/index.html', {"items": formview})


def confirm_delete(request, **kwargs):
    formview = kwargs['form']
    deleted_view = kwargs['form'].deleted_objects
    if request.method == 'POST':
        formview.save()
        return redirect('start_page')
    else:
        return render(request, 'django_app/index.html', {"items": deleted_view})