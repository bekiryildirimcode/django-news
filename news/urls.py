from django.contrib import admin
from django.urls import path
from news.views import HomeView,CategoryView,CategoryDeleteView,NewsView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', HomeView.as_view(),name="homepage"),
    path('category/',login_required(CategoryView.as_view()) ,name="categoryadd"),
     path('news/add',login_required(NewsView.as_view()) ,name="newsadd"),
    path('category/delete/<slug:slug>',login_required(CategoryDeleteView.as_view()) ,name="categorydelete"),
]

