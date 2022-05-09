from django.contrib import admin
from todo.models import ToDoDate, Items

admin.site.register(Items)
admin.site.register(ToDoDate)

# Register your models here.
