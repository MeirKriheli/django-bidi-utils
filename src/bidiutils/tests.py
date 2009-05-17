from django.test import TestCase
from django.utils.translation import activate, get_language
from django.template import Template, RequestContext, TemplateSyntaxError
from context_processors import bidi

class ContextTest(TestCase):
    """Test for correct context processor"""

    def setUp(self):
        # keep orig language
        self.orig_language = get_language()

    def tearDown(self):
        # restore orig language
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

    def render(self, template, **kwargs):
        """Return the rendering of a given template"""
        return Template(template).render(RequestContext({}, kwargs)).strip()

    def test_ltr_template(self):
        """Test for ltr variables in template"""
        activate('en-us')
        response = self.render('{{LANGUAGE_START}} {{LANGUAGE_END}} {{LANGUAGE_DIRECTION}} ' +\
            '{{LANGUAGE_MARKER}}'
        )

        self.failUnlessEqual(response, 'left right ltr &lrm;')

    def test_rtl_template(self):
        """Test for rtl variables in template"""
        activate('he')
        response = self.render('{{LANGUAGE_START}} {{LANGUAGE_END}} {{LANGUAGE_DIRECTION}} ' +\
            '{{LANGUAGE_MARKER}}'
        )

        self.failUnlessEqual(response, u'right left rtl &rlm;')

    def test_add_direction_rtl(self):
        """Test add_direction template filter when language is rtl"""
        template = u'{% load bidiutils_tags %}'+ \
            '{{image|add_direction}}\n' + \
            '{{image|add_direction:"rtl_only"}}\n' + \
            '{{image|add_direction:"both"}}\n' + \
            '{{image|add_direction:"ltr_only"}}'

        ctx = {'image':'/media/img/arrow.png'}

        activate('he')

        response = self.render(template, **ctx)
        self.failUnlessEqual(response,
            u'/media/img/arrow_rtl.png\n'+\
            u'/media/img/arrow_rtl.png\n'+\
            u'/media/img/arrow_rtl.png\n'+\
            u'/media/img/arrow.png'
        )

    def test_add_direction_ltr(self):
        """Test add_direction template filter when language is ltr"""
        template = u'{% load bidiutils_tags %}'+ \
            '{{image|add_direction}}\n' + \
            '{{image|add_direction:"rtl_only"}}\n' + \
            '{{image|add_direction:"both"}}\n' + \
            '{{image|add_direction:"ltr_only"}}'

        ctx = {'image':'/media/img/arrow.png'}

        activate('en')

        response = self.render(template, **ctx)
        self.failUnlessEqual(response,
            u'/media/img/arrow.png\n'+\
            u'/media/img/arrow.png\n'+\
            u'/media/img/arrow_ltr.png\n'+\
            u'/media/img/arrow_ltr.png'
        )

    def test_add_direction_invalid_arg(self):
        """add_direction should raise an exception in case arg is not in
        ["rtl_only", "both", "ltr_only"]

        """
        template = u'{% load bidiutils_tags %}'+ \
            '{{image|add_direction:"bla"}}'
        activate('en')
        ctx = {'image':'/media/img/arrow.png'}
        self.failUnlessRaises(TemplateSyntaxError, self.render, template, **ctx)
