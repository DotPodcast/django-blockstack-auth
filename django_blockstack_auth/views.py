from blockchainauth import AuthResponse
from jwt import DecodeError
from django.conf import settings as site_settings
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http.response import (
    HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
)

from django.utils.http import urlencode
from django.views.generic.base import TemplateView, View
from mimetypes import guess_type
from urlparse import urljoin
from . import utils, settings
import json


class LoginView(TemplateView):
    template_name = 'blockstack/login.html'

    def get_context_data(self):
        return {
            'callback_url': u'%s?%s' % (
                self.request.build_absolute_uri(
                    reverse('blockstack:callback')
                ),
                urlencode(
                    {
                        'next': (
                            self.request.GET.get('next') or
                            site_settings.LOGIN_REDIRECT_URL
                        )
                    }
                )
            ),
            'manifest_url': self.request.build_absolute_uri(
                reverse('blockstack:manifest')
            )
        }


class CallbackView(View):
    def get(self, request):
        next_url = request.GET.get('next')
        ar = request.GET.get('authResponse', u'')

        try:
            response = AuthResponse.decode(ar)
        except DecodeError:
            return HttpResponseBadRequest('Bad authentication response')

        payload = response['payload']
        user = utils.get_or_create_user(payload)
        login(self.request, user)

        return HttpResponseRedirect(next_url)


class LogoutView(TemplateView):
    template_name = 'blockstack/logout.html'

    def get_context_data(self):
        return {
            'next_url': self.request.GET.get('next') or '/'
        }


class ManifestView(View):
    def get(self, request):
        data = {
            'name': settings.APP_NAME,
            'start_url': request.META['HTTP_HOST'],
            'description': settings.APP_DESCRIPTION,
            'icons': [
                {
                    'src': urljoin(
                        request.build_absolute_uri(),
                        settings.APP_ICON
                    ),
                    'sizes': '192x192',
                    'type': guess_type(settings.APP_ICON)[0]
                }
            ]
        }

        response = HttpResponse(
            json.dumps(data),
            content_type='application/json'
        )

        response['Access-Control-Allow-Origin'] = '*'
        return response
