
Django Bidi Utils
=================

Provides context processors and filters for handling `Bi-directional`_ (BiDi) in django templates.

.. _Bi-directional: http://en.wikipedia.org/wiki/Bi-directional_text

Context processors
------------------

Add it to `TEMPLATE_CONTEXT_PROCESSORS`_ in your project's settings.py. e.g::

  ("django.core.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "bidiutils.context_processors.bidi",)

.. _TEMPLATE_CONTEXT_PROCESSORS: http://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors

The context processor defines the following template variables:

* `LANGUAGE_DIRECTION`: Direction of current language (`ltr` or `rtl`)
* `LANGUAGE_START`: Start of language layout (`right` for RTL, `left` for LTR)
* `LANGUAGE_END` -- End of language layout (`left` for RTL, `right` for LTR)
* `LANGUAGE_MARKER` -- Language marker entity (`&rlm;` for RTL, `&lrm;` for LTR)


Filters
--------

add_direction
~~~~~~~~~~~~~

Adds direction to the element

:arguments:

    arg

        * rtl_only: Add the direction only in case of a
          right-to-left language (default)
        * both: add the direction in both case
        * ltr_only: Add the direction only in case of a
          left-to-right language

{{image_name|add_direction}} when image_name is 'start_arrow.png'
results in 'start_arrow_rtl.png' in case of RTL language, and
'start_arrow.png' or 'start_arrow_ltr.png' depends on `arg`
value.


Notes
-----

In this document:

RTL
    Right-to-Left written language (e.g: Hebrew, Arabic)

LTR
    Left-to-Right written language (e.g: English, French)

