from django_app.models.BaseModel import BaseModel
from django_app.models.ScheduleRecord import Record, BaseModel
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
import requests


class StartPage(TemplateView):
    template_name = 'django_app/index.html'

    def get_context_data(self, **kwargs):
        result = Record.objects.filter(created__month=timezone.now().month)
        users = User.objects.all()
        return {'items': result, 'users': users}
