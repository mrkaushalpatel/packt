from django import  forms
from modelForms.models import Project

class ProjectForm(forms.ModelForm):

    model = Project
    fields = '__all__'
