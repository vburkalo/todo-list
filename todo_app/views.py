from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
)
from django.urls import reverse_lazy

from todo_app.forms import TaskForm, TagForm
from todo_app.models import Task, Tag


class HomeView(ListView):
    model = Task
    template_name = "todo_list/home.html"
    context_object_name = "tasks"
    ordering = ["-done", "-datetime"]


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    pk_url_kwarg = "task_id"
    success_url = reverse_lazy("todo_list:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    pk_url_kwarg = "task_id"
    success_url = reverse_lazy("todo_list:home")


class TaskToggleDoneView(RedirectView):
    pattern_name = "todo_list:home"

    def get_redirect_url(self, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["task_id"])
        task.done = not task.done
        task.save()
        return super().get_redirect_url(*args, **kwargs)


class TagListView(ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    pk_url_kwarg = "tag_id"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo_list/tag_confirm_delete.html"
    pk_url_kwarg = "tag_id"
    success_url = reverse_lazy("todo_list:tag-list")
