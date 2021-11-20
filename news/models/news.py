
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from news.models import Category
from django.utils import timezone

from ckeditor.fields import RichTextField
class NewsModel(models.Model):
    image=models.ImageField(upload_to="news_image",null=False, default="Some String")
    category=models.ManyToManyField(Category,related_name="news")
    name=models.TextField(null=False)
    slug=AutoSlugField(populate_from="name",unique=True,null=True)
    title=models.TextField(unique=True,null=True)
    description = RichTextField(null=False,default="Some String")
    data=models.JSONField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author",null=True)
    videolink=models.CharField(max_length=250, unique=False,null=True)
    breking= models.BooleanField(default=True)
    slider= models.BooleanField(default=True)
    click =models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:

        verbose_name = 'NewsModel'
        verbose_name_plural = 'NewsModels'

    def __str__(self):
        return self.name
        
