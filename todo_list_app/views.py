from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_list_app.forms import TagForm, TaskForm
from todo_list_app.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list_app:tag-list")
    form_class = TagForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list_app:tag-list")
    form_class = TagForm


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list_app:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list_app:task-list")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:task-list")


class TaskCompletedView(generic.View):
    model = Task

    def post(self, request, pk: int) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()

        return HttpResponseRedirect(
            reverse("todo_list_app:task-list")
        )
