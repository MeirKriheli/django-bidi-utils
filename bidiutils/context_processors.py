"""Context processors for BiDi"""

def bidi(request):
    """Adds to the context BiDi related variables

    LANGUAGE_DIRECTION -- Direction of the current language ('ltr' or 'rtl')
    LANGUAGE_START -- Start of the language layout ('right' for rtl, 'left'
                      for 'ltr')
    LANGUAGE_END -- End of the language layout ('left' for rtl, 'right'
                      for 'ltr')

    """

    from django.utils import translation
    if translation.get_language_bidi():
        extra_context = {
            'LANGUAGE_DIRECTION':'rtl',
            'LANGUAGE_START':'right',
            'LANGUAGE_END':'left',
        }
    else:
        extra_context = {
            'LANGUAGE_DIRECTION':'ltr',
            'LANGUAGE_START':'left',
            'LANGUAGE_END':'right',
        }

    return extra_context