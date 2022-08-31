from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


