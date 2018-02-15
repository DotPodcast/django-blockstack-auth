from django.conf import settings as site_settings


APP_NAME = getattr(
    site_settings, 'BLOCKSTACK_APP_NAME', 'Hello Blockstack'
)

APP_DESCRIPTION = getattr(
    site_settings,
    'BLOCKSTACK_APP_DESCRIPTION',
    'A simple demo of Blockstack Auth'
)

APP_ICON = (site_settings.STATIC_URL or '/static/') + getattr(
    site_settings,
    'BLOCKSTACK_APP_ICON',
    'blockstack/img/icon-192x192.png'
)
