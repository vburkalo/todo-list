from django import forms
from todo_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["deadline"].input_formats = ("%Y-%m-%dT%H:%M",)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
