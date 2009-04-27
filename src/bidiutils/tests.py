from django.test import TestCase
from django.utils.translation import activate, get_language
from context_processors import bidi

class ContextTest(TestCase):
    """Test for correct context processor"""

    def setUp(self):
        # keep orig language
        self.orig_language = get_language()

    def tearDown(self):
        # resotore orig language
        activate(self.orig_language)

    def test_ltr(self):
        """Test for left-to-right languages"""
        activate('en-us')

        ctx = bidi({})
        self.failUnlessEqual(ctx, {
            'LANGUAGE_END': 'right',
            'LANGUAGE_START': 'left',
            'LANGUAGE_DIRECTION': 'ltr',
            'LANGUAGE_MARKER': '&lrm;',
        })

    def test_rtl(self):
        """Test for right-to-left languages"""
        activate('he')

        ctx = bidi({})
        self.failUnlessEqual(ctx, {
            'LANGUAGE_END': 'left',
            'LANGUAGE_START': 'right',
            'LANGUAGE_DIRECTION': 'rtl',
            'LANGUAGE_MARKER': '&rlm;',
        })
