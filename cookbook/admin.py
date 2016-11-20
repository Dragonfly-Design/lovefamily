from django.contrib import admin

# Register your models here.

from .models import Document, Page

admin.site.register(Document)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'page_number', 'title', 'img_sm_url', 'updated')
    ordering = ('page_number',)
    search_fields = ('page_number', 'title', 'search_text',)




