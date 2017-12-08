#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-blockstack-auth
------------

Tests for `django-blockstack-auth` views module.
"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from django_blockstack_auth.views import LoginView, CallbackView, LogoutView


class LoginViewTest(StaticLiveServerTestCase):
    def test_view(self):
        client = Client()
        response = client.get('%s/blockstack/login/' % self.live_server_url)
        self.assertEqual(
            response.template_name,
            ['blockstack/login.html']
        )


class LogoutViewTest(StaticLiveServerTestCase):
    def test_view(self):
        client = Client()
        response = client.get('%s/blockstack/logout/' % self.live_server_url)
        self.assertEqual(
            response.template_name,
            ['blockstack/logout.html']
        )

# TODO: Find a way to test the full login/logout flow using the
#       Blockstack portal
