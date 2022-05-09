from django import forms
from todo.models import Items


class OneItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = (
            'id',
            'name',
            'status',
            'group',
            'order',
        )
