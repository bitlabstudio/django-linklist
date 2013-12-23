"""Tests for the templatetags of the linklist app."""
from django.test import TestCase

from . import factories
from ..templatetags import linklist_tags


class GetLinklistTestCase(TestCase):
    """Tests for the ``get_linklist`` assignment tag."""
    longMessage = True

    def test_tag_without_category(self):
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        result = linklist_tags.get_linklist(4)
        self.assertEqual(result.count(), 4, msg=(
            'Should return the desired amount of links'))

    def test_tag_with_category(self):
        cat1 = factories.LinkCategoryFactory(slug='foo')
        cat1.save()
        cat2 = factories.LinkCategoryFactory(slug='bar')
        cat2.save()
        link1 = factories.LinkFactory(category=cat1)
        link1.save()
        link2 = factories.LinkFactory(category=cat2)
        link2.save()
        result = linklist_tags.get_linklist(4, categories='foo')
        self.assertEqual(result[0].category, cat1, msg=(
            'Should return only links with the desired category'))

    def test_tag_with_multiple_categories(self):
        cat1 = factories.LinkCategoryFactory(slug='foo')
        cat1.save()
        cat2 = factories.LinkCategoryFactory(slug='bar')
        cat2.save()
        link1 = factories.LinkFactory(category=cat1)
        link1.save()
        link2 = factories.LinkFactory(category=cat2)
        link2.save()
        result = linklist_tags.get_linklist(4, categories='foo,bar')
        self.assertEqual(result.count(), 2, msg=(
            'Should return links for all desired categories'))
