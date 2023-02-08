from django_app.models.BaseModel import BaseModel
from django_app.models.ScheduleRecord import Record, BaseModel
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime


class StartPage(TemplateView):
    template_name = 'django_app/index.html'

    def get_context_data(self, **kwargs):
        result = Record.objects.all()
        return {'items': [
            {
                'user': items.holder,
                'start_date': items.created,
                'description' : items.description,
                'status': items.status,
            }
            for items in result
        ]
        }
