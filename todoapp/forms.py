from django import forms

class TaskCreateForm(forms.form):
    task_name=forms.CharField(max_length=120)
    date=forms.CharField(max_length=50)
    status=forms.CharField(max_length=60)