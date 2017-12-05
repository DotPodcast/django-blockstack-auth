# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_blockstack_auth.urls import urlpatterns as django_blockstack_auth_urls

urlpatterns = [
    url(r'^', include(django_blockstack_auth_urls, namespace='django_blockstack_auth')),
]
