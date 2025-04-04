from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('add/', TodoCreateView.as_view(), name='todo_add'),
    path('<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_edit'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
]