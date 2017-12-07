=============================
Django Blockstack Auth
=============================

.. image:: https://badge.fury.io/py/django-blockstack-auth.svg
    :target: https://badge.fury.io/py/django-blockstack-auth

.. image:: https://travis-ci.org/dotpodcast/django-blockstack-auth.svg?branch=master
    :target: https://travis-ci.org/dotpodcast/django-blockstack-auth

.. image:: https://codecov.io/gh/dotpodcast/django-blockstack-auth/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dotpodcast/django-blockstack-auth

Blockstack ID authentication backend for Django

Documentation
-------------

The full documentation is at https://django-blockstack-auth.readthedocs.io.

Quickstart
----------

Install Django Blockstack Auth::

    pip install django-blockstack-auth

Add it to your `INSTALLED_APPS`:

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
        url(r'^blockstack/', include(django_blockstack_auth_urls, namespace='blockstack')),
        ...
    ]

Features
--------

* Allows users to authenticate with their Blockstack ID
* Encrypts Blockstack tokens with the Django secret key

Running tests
-------------

Does the code actually work?

::

    $ pip install detox
    $ source <YOURVIRTUALENV>/bin/activate
    (myenv) $ detox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
