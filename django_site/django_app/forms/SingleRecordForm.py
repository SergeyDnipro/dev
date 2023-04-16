from django.forms import ModelForm
from django import forms
from django_app.models.ScheduleRecord import Record
from django.core.exceptions import ValidationError


class SingleRecordForm(ModelForm):
    schedule_group = forms.CharField(max_length=20, required=False, empty_value=None, label='GROUP')

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
        self.fields['description'].widget.attrs.update(size=50)
        self.fields['description'].initial = 'Description'

    # def clean_description(self):
    #     data = self.cleaned_data['description']
    #     if data != '123':
    #         raise ValidationError(' Incorrect value')
    #     return data


class SingleEditRecordForm(ModelForm):
    class Meta:
        model = Record
        fields = (
            'id',
            'holder',
            'description',
            'status',
            'schedule_group',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(size=50)
        self.fields['id'].widget.attrs.update(size=30)
        self.fields['holder'].disabled = True
        self.fields['id'].disabled = True
