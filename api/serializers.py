from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('__all__')
        read_only_fields = ("id","user", "date")

class TodoItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ("id", "title", "description")

