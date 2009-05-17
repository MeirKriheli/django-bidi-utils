"""Helper tags and filters easing the handling of bidi in templates

"""
from django import template
from django.template.defaultfilters import stringfilter
from django.utils import translation

register = template.Library()

def add_direction(value, arg=u"rtl_only"):
    """Adds direction to the element

    :arguments:
        arg
            * rtl_only: Add the direction only in case of a
              right-to-left language (default)
            * both: add the direction in both case
            * ltr_only: Add the direction only in case of a
              left-to-right language

    {{image_name|add_direction}} when image_name is 'start_arrow.png'
    results in 'start_arrow_rtl.png' in case of RTL language, and
    'start_arrow.png' or 'start_arrow_ltr.png' depends on `arg` value.

    """

    if arg == u'rtl_only':
        directions = (u'', u'_rtl')
    elif arg == u'both':
        directions = (u'_ltr', u'_rtl')
    elif arg == u'ltr_only':
        directions = (u'_ltr', u'')
    else:
        raise template.TemplateSyntaxError('add_direction can use arg with one of ["rtl_only", "both", "ltr_only"]')

    parts = value.rsplit('.', 1)
    if not len(parts):
        return value
    elif len(parts) == 1:
        return value + directions[translation.get_language_bidi()]
    else:
        return '.'.join((parts[0]+directions[translation.get_language_bidi()],parts[1]))
add_direction.is_safe = True

register.filter(add_direction)