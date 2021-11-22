from django import forms
from django.forms import fields
from news.models import NewsModel
from ckeditor.fields import RichTextField

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['videolink'].required = False
        
    description=forms.Textarea(attrs={'class': 'ckeditor','style':'width:100%'})
    class Meta:
        model=NewsModel
        fields=("image","category","name","title","description","author","videolink","breking","slider")


