from django.conf.urls.defaults import *
from galina.note.views import *

urlpatterns = patterns('',
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),

#    url(r'^$', current_datetime),
    url(r'^hello/$', hello),
  #  url(r'^current_url_view_good/$', current_url_view_good),
   # url(r'^ua_display_good2/$', ua_display_good2),
    #url(r'^display_meta/$', display_meta),
)
'''
from django.conf.urls.defaults import *
from galina.note.views import current_datetime

urlpatterns = patterns('',(r'^$', current_datetime),)
'''
''' 
from django.conf.urls.defaults import *

urlpatterns = patterns('',url(r'^$', 'note.views.current_datetime'),)
'''
