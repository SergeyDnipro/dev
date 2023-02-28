from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_app.forms.SingleRecordForm import SingleRecordForm, SingleEditRecordForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django_app.models.ScheduleRecord import Record
from django.shortcuts import render, redirect, get_object_or_404


class SingleRecordCreateView(CreateView):
    template_name = 'django_app/add_record.html'
    form_class = SingleRecordForm
    success_url = reverse_lazy('start_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['user'] = self.request.user
        # context['ids'] = [temp_id.id for temp_id in Record.objects.all()]
        return context

    def get_initial(self):
        user = self.request.user
        # user = get_object_or_404(User, id=1)
        self.initial.update({'holder': user})
        return super(SingleRecordCreateView, self).get_initial()

    # def form_valid(self, form):
    #     form.instance.holder = self.request.user
    #     return super(SingleRecordCreateView, self).form_valid(form)


class SingleRecordUpdateView(UpdateView):
    model = Record
    template_name = 'django_app/add_record.html'
    form_class = SingleEditRecordForm
    success_url = reverse_lazy('start_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


def edit_record_view(request, **kwargs):
    result = Record.objects.get(**kwargs)
    users = User.objects.all()
    user_auth = request.user.is_authenticated

    if request.method == 'GET':
        context = {
            'form': SingleEditRecordForm(instance=result),
            'users': users, 'result': result,
            'user_auth': user_auth,
                   }
        return render(request, 'django_app/add_record.html', context)
    if request.method == 'POST':
        form = SingleEditRecordForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_page', kwargs={'holder__username': form.cleaned_data['holder']}))
        else:
            return render(request, 'django_app/add_record.html', {'form': form})
