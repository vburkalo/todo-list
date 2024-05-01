from django.urls import path
from todo_app.views import (
    HomeView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleDoneView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "todo_list"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:task_id>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:task_id>/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "task/toggle/<int:task_id>/",
        TaskToggleDoneView.as_view(),
        name="task-toggle-done",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/update/<int:tag_id>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/delete/<int:tag_id>/", TagDeleteView.as_view(), name="tag-delete"),
]
