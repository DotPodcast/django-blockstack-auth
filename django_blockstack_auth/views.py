from django.views.generic.base import View
from django.http.response import HttpResponse
from mimetypes import guess_type
from urlparse import urljoin
from .utils import get_auth_url
from . import settings
import json


class LoginView(View):
    def get(self, request):
        response = HttpResponse(status=302)
        url = get_auth_url(request)
        response['Location'] = url

        return response


class ManifestView(View):
    def get(self, request):
        data = {
            'name': settings.APP_NAME,
            'start_url': request.build_absolute_uri('/'),
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
