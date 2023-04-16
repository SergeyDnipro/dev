from django_app.models.ScheduleRecord import Record
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django_app.task.msg_to_telegram import msg_to_telegram


class StartPage(TemplateView):
    template_name = 'django_app/index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.result = None
        self.msg = ''

    def get(self, request, *args, **kwargs):
        self.result = Record.objects.all().order_by('holder__username')
        for element in self.result:
            if element.status == Record.Status.COMPLETED:
                self.msg += f"Completed task - {element.created.strftime('%Y-%b-%d - %H:%m')} {element.holder} {element.description}\n"
        msg_to_telegram(self.msg)
        return super(StartPage, self).get(self)

    def get_context_data(self, **kwargs):
        # result = Record.objects.all().order_by('holder__username')
        users = User.objects.all()
        return {'items': self.result, 'users': users}
