from django.conf.urls.defaults import *
from mysite.galina.note.views import current_datetime(request)

urlpatterns = patterns('',url(r'^$', note),)
