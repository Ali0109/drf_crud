from django.db import models
from django_softdelete.models import SoftDeleteModel


class Data(SoftDeleteModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Дата"
        verbose_name_plural = "Данные"

