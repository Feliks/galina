from django.conf.urls.defaults import *
from galina.note.views import *

urlpatterns = patterns('',
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact_form/$', contact),
    url(r'^$', current_datetime),
    url(r'^hello/$', hello),
    url(r'^current_url_view_good/$', current_url_view_good),
    url(r'^ua_display_good2/$', ua_display_good2),
    url(r'^display_meta/$', display_meta),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^book_list/$', book_list),
    url(r'^events/$', events),
    url(r'^add_master/$', add_master),
    url(r'^add_master_results/$', add_master_results),
    url(r'^del_master/$', del_master),
    url(r'^del_master_results/$', del_master_results),
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
