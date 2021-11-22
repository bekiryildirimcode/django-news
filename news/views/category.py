
from news.forms import CategoryForm
from news.models import Category
from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
class CategoryView(View):
    form=CategoryForm()
    http_method_names=['get','post']
    def get(self,request):
        return render(request,'back/categoryadd.html',context={
            "form":self.form
        })
    def post(self,request):
        form=CategoryForm(request.POST)
        if form.is_valid():
            form=CategoryForm(request.POST)
            form.save()
            return redirect("categoryadd")
    
    def delete(request,slug):
        get_object_or_404(Category,slug)
        return redirect("categoryadd")


class CategoryDeleteView(DeleteView):
  
    template_name="back/category_confirm_delete.html"
    model=Category
    success_url = reverse_lazy("categoryadd")
