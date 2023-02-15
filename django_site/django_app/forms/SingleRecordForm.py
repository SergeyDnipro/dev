from django.forms import ModelForm
from django_app.models.ScheduleRecord import Record


class SingleRecordForm(ModelForm):
    class Meta:
        model = Record
        fields = (
            'holder',
            'description',
            'status',
            'schedule_group',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['holder'].disabled = True
