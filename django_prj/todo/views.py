from rest_framework import generics
from django.shortcuts import render
from django.views.generic import TemplateView
from todo.models import Items, ToDoDate
from todo.forms.ItemForm import OneItemForm
from todo.serializers.serializers import *
from todo.pagination import MyPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from todo.utils.roman_to_int import RomanToInt
from todo.tasks import foo_1, foo_2


# Сериализация обьекта - DRF - вывод одного обьекта из одной таблицы и связанных с ним обьектов из другой
class ToDoSerializerView(generics.RetrieveAPIView):
    serializer_class = ToDoSerializer
    lookup_field = 'date'
    queryset = ToDoDate.objects.all()


# Сериализация обьекта - DRF - вывод обьектов по значению ключа 'status' и запуск задания при значении 'Done'
class ItemsSerializerView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self, **kwargs):
        key = list(self.kwargs.keys())[0]
        key_val = self.kwargs[key]
        if key_val == 'Done':
            print(foo_2.delay(5, 7).get())
        return Items.objects.filter(**{key: key_val})


# Меняем "page" на "stranica" и применяем select_related
class ItemsNewPageSerializerView(generics.ListAPIView):
    serializer_class = ItemsSerializer
    pagination_class = MyPagination
    print(foo_1.delay(1, 4))

    def get_queryset(self):
        return Items.objects.select_related('group').all()


# Принимает в качестве аргумента в запросе римские цифры
class ItemsRomanSerializerView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        qs = Items.objects.select_related('group').all()
        pagin = Paginator(qs, 5)
        page = self.request.GET.get('page', 1)
        try:
            item_list = pagin.page(page)
        except PageNotAnInteger:
            try:
                item_list = pagin.page(int(RomanToInt.roman_to_int(page)))
            except EmptyPage:
                item_list = pagin.page(1)

        return item_list


# Вывод записей для УРЛа с фильтром "done" (сделано).
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


class OneItemView(TemplateView):
    template_name = 'todo/output-1.html'

    def get_context_data(self, **kwargs):
        result = Items.objects.order_by('group__date')
        return {
            'item': OneItemForm(instance=result.first())
        }

# Create your views here.
