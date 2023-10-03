from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
        labels = {
            'taskTitle': 'Title',
            'taskDescription': 'Description',
        }
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['taskTitle'].widget.attrs.update({'class': 'form-control mt-2'})
        self.fields['taskDescription'].widget.attrs.update({'class': 'form-control mt-2'})
