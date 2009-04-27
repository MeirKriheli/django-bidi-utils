Django Bidi Utils
=================

Provides context processors and helpers to ease the handling
of `Bi-directional`_ (BiDi) in django templates.

.. _Bi-directional: http://en.wikipedia.org/wiki/Bi-directional_text

Add it to `TEMPLATE_CONTEXT_PROCESORS`_ in your project's settings.py. e.g::

  ("django.core.context_processors.auth",
   "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "bidiutils.context_processors.bidi",)

.. _TEMPLATE_CONTEXT_PROCESORS: http://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors

The context processor defines the following template variables:

* `LANGUAGE_DIRECTION`: Direction of current language (`ltr` or `rtl`)
* `LANGUAGE_START`: Start of language layout (`right` for RTL, `left` for LTR)
* `LANGUAGE_END` -- End of language layout (`left` for RTL, `right` for LTR)
* `LANGUAGE_MARKER` -- Language marker entity (`&rlm;` for RTL, `&lrm;` for LTR)

In this doucment:

RTL
    Right-to-Left written language (e.g: Hebrew, Arabic)

LTR
    Left-to-Right written language (e.g: English, French)
