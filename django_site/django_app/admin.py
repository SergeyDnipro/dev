from django.contrib import admin
from django_app.models.ScheduleRecord import Record
from django_app.models.BaseModel import BaseModel


class RecordAdmin(admin.ModelAdmin):
    list_display = ('created', 'holder', 'description', 'status')
    list_display_links = ('created', 'holder')
    search_fields = ('created', 'holder__username', 'status',)


admin.site.register(Record, RecordAdmin)


# Register your models here.
