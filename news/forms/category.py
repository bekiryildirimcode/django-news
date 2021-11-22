from django import forms
from django.forms import fields
from news.models import Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=("name","parent")


