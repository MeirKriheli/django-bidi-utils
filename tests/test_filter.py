from django.template import Template, RequestContext, TemplateSyntaxError
from django.test import TestCase
from django.utils.translation import activate, get_language


class TestBidiutilsFilter(TestCase):
    """add_direction filter tests"""

    def setUp(self):
        # keep orig language
        self.orig_language = get_language()

    def tearDown(self):
        # restore orig language
        activate(self.orig_language)

    def render(self, template, **kwargs):
        """Return the rendering of a given template"""
        return Template(template).render(RequestContext({}, kwargs)).strip()

    def test_add_direction_rtl(self):
        """Test add_direction template filter when language is rtl"""
        template = (
            u'{% load bidiutils_tags %}'
            '{{image|add_direction}}\n'
            '{{image|add_direction:"rtl_only"}}\n'
            '{{image|add_direction:"both"}}\n'
            '{{image|add_direction:"ltr_only"}}'
        )

        ctx = {'image': '/media/img/arrow.png'}

        activate('he')

        response = self.render(template, **ctx)
        self.failUnlessEqual(
            response,
            u'/media/img/arrow_rtl.png\n'
            u'/media/img/arrow_rtl.png\n'
            u'/media/img/arrow_rtl.png\n'
            u'/media/img/arrow.png'
        )

    def test_add_direction_ltr(self):
        """Test add_direction template filter when language is ltr"""

        template = (
            u'{% load bidiutils_tags %}'
            '{{image|add_direction}}\n'
            '{{image|add_direction:"rtl_only"}}\n'
            '{{image|add_direction:"both"}}\n'
            '{{image|add_direction:"ltr_only"}}'
        )
        ctx = {'image': '/media/img/arrow.png'}

        activate('en')

        response = self.render(template, **ctx)

        self.failUnlessEqual(
            response,
            u'/media/img/arrow.png\n'
            u'/media/img/arrow.png\n'
            u'/media/img/arrow_ltr.png\n'
            u'/media/img/arrow_ltr.png'
        )

    def test_add_direction_invalid_arg(self):
        """add_direction should raise an exception in case arg is not in
        ["rtl_only", "both", "ltr_only"]

        """
        template = u'{% load bidiutils_tags %}{{image|add_direction:"bla"}}'
        activate('en')
        ctx = {'image': '/media/img/arrow.png'}
        self.failUnlessRaises(TemplateSyntaxError, self.render,
                              template, **ctx)
