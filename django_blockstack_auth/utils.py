from django.db import transaction
from django.contrib.auth import get_user_model
from .exceptions import AuthError


@transaction.atomic()
def get_or_create_user(payload):
    User = get_user_model()

    username = payload['username']
    email = payload['email']
    public_keys = payload['public_keys']
    profile = payload['profile']
    name = profile.get('name')

    for public_key in public_keys:
        for user in User.objects.filter(
            public_keys__key=public_key
        ).select_related():
            user.backend = 'django_blockstack_auth.backends.BlockstackBackend'
            return user

    uname = username
    i = 0

    while User.objects.filter(username=uname).exists():
        uname = '%s%d' % (
            username,
            User.objects.filter(username=uname).count() + i
        )

        i += 1

    name_parts = '', ''
    first_name, last_name = '', ''

    if name:
        name_parts = name.rsplit(' ', 1)
        if len(name_parts) < 2:
            first_name = name_parts[0]
            last_name = ''
        else:
            first_name, last_name = name_parts

    user_info = {
        'username': uname,
        'first_name': first_name,
        'last_name': last_name
    }

    if email:
        user_info['email'] = email

    user = User.objects.create(**user_info)
    for public_key in public_keys:
        user.public_keys.create(key=public_key)

    user.backend = 'django_blockstack_auth.backends.BlockstackBackend'
    return user
