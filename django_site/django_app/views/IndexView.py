from django_app.models.ScheduleRecord import Record
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django_app.task.msg_to_telegram import msg_to_telegram
from django.forms import modelformset_factory, formset_factory
from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import DeleteView


class Delete(DeleteView):
    pass


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
        print(users)
        return {'items': result, 'users': users}

    def post(self, request, *args, **kwargs):
        self.checked = self.request.POST.getlist('checkbox')
        print(self.checked)
        print(self.request.POST.get('save'))
        self.request.session['test'] = self.request.POST.get('save')
        return redirect(reverse('confirm_delete'))


def formset_view(request, **kwargs):
    changed_records = []
    formset = modelformset_factory(
        Record,
        fields=['id', 'holder', 'schedule_group', 'description', 'status'],
        can_delete=True,
        extra=0,
    )
    if 'delete' in request.POST:
        print(request.POST)
    if request.method == 'POST':
        formview = formset(request.POST)
        print(formview.is_valid())
        if formview.is_valid():
            # if 'delete' in request.POST:
            #     for el in formview.deleted_objects:
            #         print(el)
            #         el.delete()
            #     return redirect('start_page')
            formview.save(commit=False)
            request.session['rec1'] = 1
            deleted_records = formview.deleted_objects
            serialized_records = [el for el in deleted_records]
            for element in formview.changed_objects:
                changed_records.append(element[0])
            print(deleted_records)
            request.session['rec1'] = serialized_records
            return redirect(reverse('confirm_delete'))
    formview = formset()
    return render(request, 'django_app/index.html', {"items": formview})


def confirm_delete(request, **kwargs):
    formview = request.session['test']
    print(formview + 'new view')
    if request.method == 'POST':
        print(formview)
        return redirect('start_page')
    else:
        return render(request, 'django_app/index.html', {"items": formview})