from django_app.models.ScheduleRecord import Record
from django.contrib.auth.models import User
from django_app.models.ScheduleType import ScheduleType
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
import requests


class GroupPage(TemplateView):
    template_name = 'django_app/index.html'

    def get_context_data(self, **kwargs):
        result = Record.objects.filter(**kwargs)
        users = User.objects.all
        return {'items': result, 'users': users, **kwargs}


class SinglePage(TemplateView):
    template_name = 'django_app/single_view.html'

    def get_context_data(self, **kwargs):
        result = Record.objects.filter(**kwargs)
        return {'items': result, **kwargs}
