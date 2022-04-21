from django.shortcuts import render
from django.views.generic import TemplateView
from todo.models import Items


# Вывод записей для УРЛа с фильтом "done" (сделано).
def todo_out_done(request):
    items = Items.objects.filter(status=Items.Status.done)
    return render(request, 'todo/output.html', {'items': [
                    {
                        'date': items.group.date,
                        'name': items.name,
                        'order': items.order,
                        'status': items.status,
                    }
                    for items in items
                ]
    })


# Вывод всех записей для любого УРЛа
class ToDoOutAll(TemplateView):
    template_name = 'todo/output.html'

    def get_context_data(self, **kwargs):
        return {
            'items': [
                {
                    'date': items.group.date,
                    'name': items.name,
                    'order': items.order,
                    'status': items.status,
                }
                for items in Items.objects.all()
            ]
        }


# Вывод записей для УРЛов, в которых вводиться дата в формате ГГГГ-ММ-ДД, или название события, или ИД
class ToDoOutDateID(TemplateView):
    template_name = 'todo/output.html'

    def get_context_data(self, **kwargs):
        key = list(kwargs.keys())[0]
        value = kwargs[key]
        result = Items.objects.filter(**{key: value})
        if list(result):
            return {
                'items': [
                    {
                        'date': items.group.date,
                        'name': items.name,
                        'order': items.order,
                        'status': items.status,
                    }
                    for items in result
                ]
            }
        else:
            return {
                'items': 'No record'
            }
# Create your views here.
