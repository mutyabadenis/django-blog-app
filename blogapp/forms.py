from django import forms
from . import models

class CreatedArticle(forms.ModelForm):
    class Meta:
        model = models.Blogapp
        fields = ['title','slug','body','thumb']