"""Tests for the templatetags of the linklist app."""
from django.test import TestCase

from . import factories
from ..templatetags import linklist_tags


class GetLinklistTestCase(TestCase):
    """Tests for the ``get_linklist`` assignment tag."""
    longMessage = True

    def test_tag(self):
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        factories.LinkFactory().save()
        result = linklist_tags.get_linklist(4)
        self.assertEqual(result.count(), 4, msg=(
            'Should return the desired amount of links'))
