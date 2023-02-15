from django.views.generic.edit import CreateView
from django_app.forms.SingleRecordForm import SingleRecordForm
from django.urls import reverse_lazy


class SingleRecordCreateView(CreateView):
    template_name = 'django_app/add_record.html'
    form_class = SingleRecordForm
    success_url = reverse_lazy('start_page')
