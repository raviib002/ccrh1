from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from audit_log.models.fields import CreatingUserField, LastUserField
from django.db.models.deletion import CASCADE
from random import choices

# Create your models here.
class News(models.Model):
    news_headline = models.CharField(max_length=250, verbose_name=_("News Headline"))
    photo = models.ImageField(upload_to='News_photo/', default='', verbose_name=_("News Photo"))
    desc  = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    created_by = CreatingUserField(related_name = "NewsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "NewsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.news_headline
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        db_table = 'ccrh_news'
        

class Downloads(models.Model):
    download_headline = models.CharField(max_length=250, verbose_name=_("Download Headline"))
    desc  = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    created_by = CreatingUserField(related_name = "DownloadsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "DownloadsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.download_headline
    
    class Meta:
        verbose_name = "Downloads"
        verbose_name_plural = "Downloads"
        db_table = 'ccrh_downloads'
        

class QuickLink(models.Model):
    headline = models.CharField(max_length=250, verbose_name=_("Quick Link Headline"))
    photo = models.ImageField(upload_to='QuickLink_photo/', default='', verbose_name=_("Quick Link Banner"))
    link  = models.URLField(verbose_name=_("URL"))
    created_by = CreatingUserField(related_name = "QuickLinkCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "QuickLinkUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.headline
    
    class Meta:
        verbose_name = "QuickLink"
        verbose_name_plural = "QuickLink"
        db_table = 'ccrh_quick_link'
        
class Media(models.Model):
    headline = models.CharField(max_length=250, verbose_name=_("Media Headline"))
#     cover_photo = models.ImageField(upload_to='Media_cover/', default='', verbose_name=_("Quick Link Banner"))
    video  = models.FileField(upload_to='Media_video', verbose_name=_("Video"))
    created_by = CreatingUserField(related_name = "MediaCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "MediaUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.headline
    
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"
        db_table = 'ccrh_media'