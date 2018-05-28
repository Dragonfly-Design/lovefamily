from __future__ import unicode_literals
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Document(models.Model):
    title = models.TextField(blank=True, null=True)
    #pages
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.title)

class Page(models.Model):
    title = models.TextField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    img_sm_url = models.URLField(blank=True, null=True)
    img_lg_url = models.URLField(blank=True, null=True)
    ocr_search_text = models.TextField(blank=True, null=True)
    manual_search_text = models.TextField(blank=True, null=True)
    document = models.ForeignKey(Document, blank=True, null=True, related_name="pages")
    ocr = models.BooleanField(default=False)
    manual = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['page_number']

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.page_number)

    def admin_image(self):
        if self.img_sm_url:
            return mark_safe('<img src="%s" width="100"/>' % self.img_sm_url)
        else:
            return mark_safe ('<img src=""/>')


    admin_image.short_description = 'Image'
