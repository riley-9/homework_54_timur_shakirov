from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 1:
            raise ValidationError('Field musn\'t be empty')
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 1:
            raise ValidationError('Field musn\'t be empty')
        return description

