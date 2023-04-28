from django.contrib import admin

# Register your models here.
from .models import User, MonImage,Tag

admin.site.register(User)
admin.site.register(MonImage)
admin.site.register(Tag)