Installation
============

Prerequisites
-------------

.. note:: django-webp-converter requires that Pillow and its appropriate libraries are installed. Please see https://pillow.readthedocs.org/ for instructions on installing Pillow and its dependencies.

Installation
------------

Install django-webp-converter with ``pip``::

    $ pip install django-webp-converter

Add ``webp_converter`` to your INSTALLED_APPS in settings.py:

.. code-block:: python

    INSTALLED_APPS = (
	...,
        'webp_converter',
    )

Add the ``webp_support`` context processor to your list of context processors:

.. code-block:: python

    'context_processors': [
        ...,
        'webp_converter.context_processors.webp_support',
    ]


Run ``./manage.py migrate`` to add the required tables to the database.

You will also need to configure django to serve locally stored files by
configuring the ``MEDIA_URL`` and ``MEDIA_ROOT`` settings in your project's
settings.py file.

For example:

.. code-block:: python

    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

You'll probably also want to ensure that these files will be
`served during development <https://docs.djangoproject.com/en/2.2/howto/static-files/#serving-uploaded-files-in-development>`_.