# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^callback/$', views.CallbackView.as_view(), name='callback'),
    url(r'^manifest\.json$', views.ManifestView.as_view(), name='manifest')
]
