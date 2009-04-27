"""Context processors for BiDi"""

def bidi(request):
    """Adds to the context BiDi related variables

    LANGUAGE_DIRECTION -- Direction of current language ('ltr' or 'rtl')
    LANGUAGE_START -- Start of language layout ('right' for rtl, 'left'
                      for 'ltr')
    LANGUAGE_END -- End of language layout ('left' for rtl, 'right'
                      for 'ltr')
    LANGUAGE_MARKER -- Language marker entity ('&rlm;' for rtl, '&lrm'
                       for ltr)

    """
    from django.utils import translation
    from django.utils.safestring import mark_safe

    if translation.get_language_bidi():
        extra_context = {
            'LANGUAGE_DIRECTION':'rtl',
            'LANGUAGE_START':'right',
            'LANGUAGE_END':'left',
            'LANGUAGE_MARKER': mark_safe('&rlm;'),
        }
    else:
        extra_context = {
            'LANGUAGE_DIRECTION':'ltr',
            'LANGUAGE_START':'left',
            'LANGUAGE_END':'right',
            'LANGUAGE_MARKER': mark_safe('&lrm;'),
        }

    return extra_context
