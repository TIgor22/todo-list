from django.urls import path

from todo_list_app.views import TaskListView, TagListView

app_name = "todo_list_app"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
