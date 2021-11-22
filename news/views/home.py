from multiprocessing import context
from django.shortcuts import render
from django.views import View
from news.models import NewsModel
class HomeView(View):
    http_method_names=['get','post']
    def get(self,request):
        context={
            "slider":NewsModel.objects.filter(slider=True).order_by("-updated_at")[:20]
        }
        return render(request,'front/home.html',context=context)
