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
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:task_id>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:task_id>/", TaskDeleteView.as_view(), name="task_delete"),
    path(
        "task/toggle/<int:task_id>/",
        TaskToggleDoneView.as_view(),
        name="task_toggle_done",
    ),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/update/<int:tag_id>/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/delete/<int:tag_id>/", TagDeleteView.as_view(), name="tag_delete"),
]
