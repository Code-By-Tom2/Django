from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# List all todos for the logged-in user
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/todo_list.html'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

# Create a new todo
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'due_date', 'completed']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update an existing todo
class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'due_date', 'completed']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

# Delete a todo
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

# User registration view
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')