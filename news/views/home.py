from django.shortcuts import render
from django.views import View

class HomeView(View):
    http_method_names=['get','post']
    def get(self,request):
        return render(request,'front/home.html',context={})
