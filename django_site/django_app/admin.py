from django.contrib import admin
from django_app.models.ScheduleRecord import Record
from django_app.models.ScheduleType import ScheduleType
from django_app.models.BaseModel import BaseModel


class RecordAdmin(admin.ModelAdmin):
    fields = (('id', 'schedule_group'), ('holder', 'status'), 'description')

    # def get_list_display(self, request):
    #     lst = ['created', 'description', 'status']
    #     return lst
    empty_value_display = "-empty-"
    list_display = ('created', 'holder', 'description_extended', 'status', 'schedule_group')
    # list_editable = ('description',)
    list_display_links = ('created', 'holder')
    list_filter = ('holder',)
    show_full_result_count = False
    search_fields = ('created', 'holder__username', 'status',)
    list_per_page = 10

    def description_extended(self, record):
        print(record)
        if record.description == '':
            return None
        else:
            return record.description
    description_extended.short_description = 'DESCRIPTION -1'

admin.site.register(Record, RecordAdmin)
admin.site.register(ScheduleType)
# admin.site.empty_value_display = 'EMPTY'


# Register your models here.
