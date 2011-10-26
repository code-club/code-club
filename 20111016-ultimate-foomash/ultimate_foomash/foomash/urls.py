from django.conf.urls.defaults import *
from django.views.generic import ListView
from foomash.models import Category

urlpatterns = patterns('',
	url(r'^(\d+)/$', 'foomash.views.mash'),
	url(r'^vote/$', 'foomash.views.vote'),
	url(r'^$', ListView.as_view(model=Category))
)