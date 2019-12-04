Usage
=====

Showing WebP images
-------------------

Load the webp_converter template tag in your template::

   {% load webp_converter %}

Replace usage of the ``static`` tag with the ``static_webp`` tag. For example::

    <img src="{% static_webp 'img/hello.jpg' %}">

The user will be shown a WebP version of the image if their browser supports it (currently Chrome & Opera). Otherwise, they will be shown the original static file.

You can also specify the quality of the WebP image. For example::

    <img src="{% static_webp 'img/hello.jpg' 70 %}">


Clearing the cache
------------------

Clear the cache and delete the WebP images folder by running the ``manage.py`` command::

    ./manage.py clear_webp_cache

By default this will display a confirmation prompt. If you would like to clear
the cache without receiving any prompts, you can run::

    ./manage.py clear_webp_cache --no-input

