from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=False)
    slug =AutoSlugField(populate_from='name',unique=True,null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    