from pyexpat import model
from django.forms import ModelForm
from .models import Project


class ProjectForms(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link', 'tags']
