========
Usage
========


Settings
-------------


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


Template context variables
-----------------------------

If you've added `bidiutils.context_processors.bidi` to
`TEMPLATE_CONTEXT_PROCESSORS` settings, you'll have additional variables in the
template context for templates using a `RequestContext`_:

`LANGUAGE_DIRECTION`
    Direction of current language (`ltr` or `rtl`). The 
    following common idiom:

    .. code-block:: django

        {% load i18n %}<html dir="{{ LANGUAGE_BIDI|yesno:"rtl,ltr" }}">

    Can be re-written as:

    .. code-block:: django

        {% load i18n %}<html dir="{{LANGUAGE_DIRECTION}}">

`LANGUAGE_START`
    Start of language layout (`right` for RTL, `left` for LTR).
    Useful in cases you want to align elements with inline style etc:

    .. code-block:: django
    
        <div style="float:{{LANGUAGE_START}}">

`LANGUAGE_END`
    End of language layout (`left` for RTL, `right` for LTR).  Just like
    `LANGUAGE_START`, but denotes the other side. A sample usage with
    `Bootstrap's glyphicons`_ to display an arrow going from language start to end:

    .. code-block:: django

        <span class="glyphicon glyphicon-arrow-{{ LANGUAGE_END }}"></span>

`LANGUAGE_MARKER`
    Language marker entity (`&rlm;` for RTL, `&lrm;` for LTR). Those marker are
    inserted into a location to make an enclosed weak character inherit its
    writing direction.

    Those are important to keep the flow correct in case of a weak directional
    character between to elements of the other direction. Take this template
    fragment for example:

    .. code-block:: django

        {{ user1.full_name }}: {{post1.title}}
        {{ user2.full_name }}: {{post2.title}}

    assuming your current language's direction is RTL, and user2's full name and
    post title are in LTR (e.g: both in English) while user one's are RTL The
    result will be rendered as (using UPPERCASE without actual content do
    demonstrate)::

       USER1_POST_TITLE  :USER1_FULLNAME
       USER2_FULLNAME: USER2_POST_TITLE

    This is because the ':' is weak character inheriting the direction for
    surrounding element(s). Inserting the current language marker ensures the
    correct layout

    .. code-block:: django

        {{ user1.full_name }}{{LANGUAGE_MARKER}}: {{post1.title}}
        {{ user2.full_name }}{{LANGUAGE_MARKER}}: {{post2.title}}

    For more information see `Bi-Directional text - Unicode support`_.


.. _RequestContext: https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.RequestContext
.. _Bi-Directional text - Unicode support: http://en.wikipedia.org/wiki/Bi-directional_text#Unicode_support
.. _Bootstrap's glyphicons: http://getbootstrap.com/components/#glyphicons

`add_direction` filter
-------------------------

Adds direction to the element. Make sure to load `bidiutils_tags` to use the
filter which accepts a single, optional, argument:

`rtl_only` 
    Add the direction only in case of a right-to-left language. The default if
    no argument is passed.

`both`
    Add the direction in both cases

`ltr_only`
    Add the direction only in case of a left-to-right language


Assuming the current language is RTL, and `image` in the context is
`"arrow.png"`:

.. code-block:: django

    {% load bidiutils_tags %}

    <img src="{{image|add_direction}}" alt="arrow">
    <img src="{{image|add_direction:"rtl_only"}}" alt="arrow">
    <img src="{{image|add_direction:"both"}}" alt="arrow">
    <img src="{{image|add_direction:"ltr_only"}}" alt="arrow">


The rendered result will be:

.. code-block:: html

    <img src="/media/img/arrow_rtl.png" alt="arrow">
    <img src="/media/img/arrow_rtl.png" alt="arrow">
    <img src="/media/img/arrow_rtl.png" alt="arrow">
    <img src="/media/img/arrow.png" alt="arrow">


On the other hand, Assuming the current language is LTR, and `image` in the
context is `"arrow.png"`, the rendered result of the above template would be:

.. code-block:: html

    <img src="/media/img/arrow.png" alt="arrow">
    <img src="/media/img/arrow.png" alt="arrow">
    <img src="/media/img/arrow_ltr.png" alt="arrow">
    <img src="/media/img/arrow_ltr.png" alt="arrow">
