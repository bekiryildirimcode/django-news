from news.forms import CategoryForm,NewsForm
from news.models import Category
from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
class NewsView(View):
    form=NewsForm()
    http_method_names=['get','post']
    def get(self,request):
        return render(request,'back/categoryadd.html',context={
            "form":self.form
        })