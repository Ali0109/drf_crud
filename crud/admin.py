from django.contrib import admin
from django.contrib.auth.models import User

from crud.models import *


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "phone",
        "region",
        "country",
    ]

