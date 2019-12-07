Changelog
============

0.2.1 (2019-12-07)
------------------

* Remove duplicate deletion of WebP folder in the `clear_webp_cache` command.

0.2.0 (2019-12-04)
------------------

* Switch to MIT license
* Fix bug where duplicate WebPImage models could be created due to the
  non-uniqueness of nullable fields (https://github.com/tmiller02/django-webp-converter/issues/1).
* Change the default behaviour of the 'clear_webp_cache' command to
  prompt for user confirmation before deleting the WebP image folder.
* Restructure project to split the webp_converter app out of the sample project
* Regenerate sample project using Django 3.0.
