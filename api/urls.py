from django.urls import path
from .views import TodoItemList, TodoItemDetail

urlpatterns = [
    path('', TodoItemList.as_view()),
    path('<int:pk>/', TodoItemDetail.as_view())
]