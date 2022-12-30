from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Part(MPTTModel):
    code = models.CharField(max_length=9, default="")
    name = models.CharField(max_length=128, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['code']

    def __str__(self):
        return self.name

