from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.SuperUser)
admin.site.register(models.Trip)