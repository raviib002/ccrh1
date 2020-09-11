from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms_plugins.models import (#NewsPluginModel,
                                #DownloadsPluginModel,
                                #QuickLinkPluginModel,
                                MediaPluginModel,
                                )

# @plugin_pool.register_plugin
# class NewsPlugin(CMSPluginBase):
#     model = NewsPluginModel  #If the plugin requires per-instance settings, then this setting must be set to a model that inherits from CMSPlugin
#     name = _("News Plugin")
#     render_template = "cms/news.html"
#     cache = False
#     
#     def render(self, context, instance, placeholder):
#         context.update({'instance': instance})
#         return context
    
        
@plugin_pool.register_plugin
class MediaPlugin(CMSPluginBase):
    model = MediaPluginModel  #If the plugin requires per-instance settings, then this setting must be set to a model that inherits from CMSPlugin
    name = _("Media Plugin")
    render_template = "cms/media.html"
    cache = False
    
    
# @plugin_pool.register_plugin
# class QuickLinksPlugin(CMSPluginBase):
#     model = QuickLinkPluginModel  #If the plugin requires per-instance settings, then this setting must be set to a model that inherits from CMSPlugin
#     name = _("Quick Links Plugin")
#     render_template = "cms/quick_link.html"
#     cache = False
#     
# @plugin_pool.register_plugin
# class DownloadsPlugin(CMSPluginBase):
#     model = DownloadsPluginModel  #If the plugin requires per-instance settings, then this setting must be set to a model that inherits from CMSPlugin
#     name = _("Downloads Plugin")
#     render_template = "cms/news_download.html"
#     cache = False