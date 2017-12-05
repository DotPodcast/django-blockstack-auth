=====
Usage
=====

To use Django Blockstack Auth in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_blockstack_auth.apps.DjangoBlockstackAuthConfig',
        ...
    )

Add Django Blockstack Auth's URL patterns:

.. code-block:: python

    from django_blockstack_auth import urls as django_blockstack_auth_urls


    urlpatterns = [
        ...
        url(r'^', include(django_blockstack_auth_urls)),
        ...
    ]
