#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-bidi-utils
------------

Tests for `bidiutils` context processors.
"""
import unittest

from django.template import Template, RequestContext
from django.utils.translation import activate, get_language

from bidiutils.context_processors import bidi


class TestBidiutilsContext(unittest.TestCase):

    def setUp(self):
        self.orig_language = get_language()  # keep original language

    def tearDown(self):
        activate(self.orig_language)  # restore original language

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
        response = self.render(
            '{{LANGUAGE_START}} {{LANGUAGE_END}} {{LANGUAGE_DIRECTION}} '
            '{{LANGUAGE_MARKER}}'
        )

        self.failUnlessEqual(response, 'left right ltr &lrm;')

    def test_rtl_template(self):
        """Test for rtl variables in template"""
        activate('he')
        response = self.render(
            '{{LANGUAGE_START}} {{LANGUAGE_END}} {{LANGUAGE_DIRECTION}} '
            '{{LANGUAGE_MARKER}}'
        )

        self.failUnlessEqual(response, u'right left rtl &rlm;')
