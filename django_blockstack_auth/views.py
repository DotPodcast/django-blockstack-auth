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

