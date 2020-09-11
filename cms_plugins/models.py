from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.db.models.deletion import CASCADE
from master.models import (News,
                           Downloads,
                           QuickLink,
                           Media,
                           )


# class NewsPluginModel(CMSPlugin):
#     news = models.ForeignKey(News, on_delete=CASCADE)
# 
#     def __str__(self):
#         return self.news.news_headline
#     
# class DownloadsPluginModel(CMSPlugin):
#     downloads = models.ForeignKey(Downloads, on_delete=CASCADE)
# 
#     def __str__(self):
#         return self.downloads.download_headline
#     
# class QuickLinkPluginModel(CMSPlugin):
#     quick_link = models.ForeignKey(QuickLink, on_delete=CASCADE)
# 
#     def __str__(self):
#         return self.quick_link.headline
    
class MediaPluginModel(CMSPlugin):
    media = models.ForeignKey(Media, on_delete=CASCADE)

    def __str__(self):
        return self.media.headline