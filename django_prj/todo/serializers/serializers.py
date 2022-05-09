from rest_framework import views, serializers, generics
from todo.models import Items, ToDoDate


class ItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = (
            'id',
            'name',
            'group_id',
            'order',
            'status',
        )


class ToDoSerializer(serializers.ModelSerializer):
    items_serialized = ItemsSerializer(many=True)

    class Meta:
        model = ToDoDate
        fields = (
            'id',
            'date',
            'items_serialized',

        )
