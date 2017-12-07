from django.db import transaction
from django.contrib.auth import get_user_model
from .exceptions import AuthError
from .models import UserPublicKey, UserPrivateKey


@transaction.atomic()
def get_or_create_user(payload):
    User = get_user_model()

    username = payload['username']
    email = payload['email']
    public_keys = payload['public_keys']
    private_key = payload['private_key']
    profile = payload['profile']
    name = profile['name']

    # Find user by public/private key pair
    for public_key in public_keys:
        for upk in UserPublicKey.objects.filter(
            key=public_key
        ).select_related():
            if upk.private_key.key == private_key:
                user = upk.private_key.user
                user.backend = 'django_blockstack_auth.backends.BlockstackBackend'
                return user

            # Public key matches, but private key doesn't
            raise AuthError('Public and private keys don\'t match.')

    # Create a new user and assign a new public/private key pair
    uname = username
    i = 0
    while User.objects.filter(username=uname).exists():
        uname = username + User.objects.filter(username=uname).count() + i

    name_parts = '', ''
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
    upk = UserPrivateKey.objects.create(
        user=user,
        key=private_key
    )

    for public_key in public_keys:
        upk.public_keys.create(key=public_key)

    user.backend = 'django_blockstack_auth.backends.BlockstackBackend'
    return user
