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


Additionally, you may also want to configure the ``MEDIA_URL`` and ``MEDIA_ROOT`` settings for your project in settings.py. For example:

.. code-block:: python

    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')