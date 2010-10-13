from django.conf.urls.defaults import *
from galina.note.views import *

urlpatterns = patterns('',(r'^hello/$', hello),)
urlpatterns = patterns('',(r'^current_url_view_good/$', current_url_view_good),)
urlpatterns = patterns('',(r'^ua_display_good2/$', ua_display_good2),)
urlpatterns = patterns('',(r'^display_meta/$', display_meta),)
'''
from django.conf.urls.defaults import *
from galina.note.views import current_datetime

urlpatterns = patterns('',(r'^$', current_datetime),)
'''
''' 
from django.conf.urls.defaults import *

urlpatterns = patterns('',url(r'^$', 'note.views.current_datetime'),)
'''
