# Generated by Django 3.2.9 on 2021-11-19 19:57

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='description',
            field=ckeditor.fields.RichTextField(default='Some String'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(default='Some String', upload_to='news_image'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='title',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='category',
            field=models.ManyToManyField(related_name='news', to='news.Category'),
        ),
    ]
