=============================
django-bidi-utils
=============================

.. image:: https://badge.fury.io/py/django-bidi-utils.png
    :target: http://badge.fury.io/py/django-bidi-utils

.. image:: https://travis-ci.org/MeirKriheli/django-bidi-utils.png?branch=master
        :target: https://travis-ci.org/MeirKriheli/django-bidi-utils

.. image:: https://pypip.in/d/django-bidi-utils/badge.png
        :target: https://crate.io/packages/django-bidi-utils?version=latest


Provides context processors and filters for handling `Bi-directional`_ (BiDi) in
django templates, adding some needed functionality to Django's LANGUAGE_BIDI_
template var.


.. _Bi-directional: http://en.wikipedia.org/wiki/Bi-directional_text
.. _LANGUAGE_BIDI: https://docs.djangoproject.com/en/dev/topics/i18n/translation/#other-tags


Documentation
-------------

The full documentation is at http://django-bidi-utils.rtfd.org.

Quickstart
----------

Install django-bidi-utils::

    pip install django-bidi-utils

To use it in a Django project add `bidiutils` the project's `INSTALLED_APPS`_
setting::

    INSTALLED_APPS = (
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        ...
        "bidiutils",
        ...
    )

To enable the context processor, add it to `TEMPLATE_CONTEXT_PROCESSORS`_
settings::

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        ...
        "bidiutils.context_processors.bidi",
    )

.. _TEMPLATE_CONTEXT_PROCESSORS: http://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
.. _INSTALLED_APPS: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-INSTALLED_APPS

Features
--------

* Context processor adding to templates passed a RequestContext BiDi releated
  variables.
* `add_direction` template filter, for adding direction to media resource
  (images, stylesheets, etc)
