from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('lonelyryan.bot.views',
    url(r'message/$', 'message'),
)

