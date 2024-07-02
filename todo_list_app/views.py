from django.shortcuts import render
from django.views import generic

from todo_list_app.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"
