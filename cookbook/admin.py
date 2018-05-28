from django.contrib import admin

# Register your models here.

from .models import Document, Page

admin.site.register(Document)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_image', 'page_number', 'title', 'search_text', 'img_sm_url', 'img_lg_url', 'ocr', 'manual',
                    'updated')
    list_editable = ('page_number', 'title', 'search_text', 'img_sm_url', 'img_lg_url', 'ocr', 'manual',)
    list_filter = ('ocr', 'manual',)
    ordering = ('page_number',)
    search_fields = ('page_number', 'title', 'search_text',)




