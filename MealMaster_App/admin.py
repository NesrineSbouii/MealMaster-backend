from django.contrib import admin

# Register your models here.
from .models import MonImage,Tag

admin.site.register(MonImage)
admin.site.register(Tag)