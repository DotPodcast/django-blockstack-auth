from blockchainauth import AuthRequest
from pybitcoin.privatekey import BitcoinPrivateKey
from django.core.urlresolvers import reverse
from django.conf import settings


def get_auth_url(request):
    private_key = BitcoinPrivateKey()
    data = dict(
        private_key=private_key.to_hex(),
        domain_name='localhost:8000',
        manifest_uri=request.build_absolute_uri(
            reverse('blockstack:manifest')
        ),
        redirect_uri=request.build_absolute_uri(settings.LOGIN_REDIRECT_URL),
        scopes=['store_write']
    )

    auth_request = AuthRequest(**data)
    return auth_request.redirect_url()
