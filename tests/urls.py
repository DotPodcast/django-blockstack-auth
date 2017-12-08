# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django_blockstack_auth.urls import urlpatterns as blockstack_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^blockstack/', include(blockstack_urls, namespace='blockstack'))
] + staticfiles_urlpatterns()
