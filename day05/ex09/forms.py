from django import forms
from django.forms import ModelForm
from .models import movies

class UpdateForm(forms.ModelForm): 
    class Meta:
        model = movies
        # fields = ["title"]
        # fields = '__all__'
        fields = [ 
            "episode_nb",
            # "title", 
            "opening_crawl",
        ] 
    title = forms.ModelChoiceField(queryset=movies.objects.all())
    # openin_crawl = forms.Textarea()