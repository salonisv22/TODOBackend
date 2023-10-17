from rest_framework import generics

from .models import TodoItem
from .serializers import TodoItemSerializer, TodoItemListSerializer

class TodoItemList(generics.ListCreateAPIView):
    serializer_class = TodoItemListSerializer

    def get_queryset(self):
        queryset = TodoItem.objects.all()
        userFromQuery = self.request.query_params.get('user')
        if userFromQuery is not None:
            queryset = queryset.filter(user = userFromQuery)    
        return queryset


class TodoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()