from django.conf.urls.defaults import *
from galina.note.views import current_datetime

urlpatterns = patterns('',(r'^$', current_datetime),)

''' 
from django.conf.urls.defaults import *

urlpatterns = patterns('',url(r'^$', 'note.views.current_datetime'),)
'''
