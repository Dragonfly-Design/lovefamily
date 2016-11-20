from django.contrib import admin

# Register your models here.

from .models import Document, Page

admin.site.register(Document)
admin.site.register(Page)


