"""Tests for the models of the ``linklist`` app."""
from django.test import TestCase

from .. import models


class LinkTestCase(TestCase):
    """Tests for the ``Link`` model class."""
    longMessage = True

    def test_model(self):
        """Test if the ``Link`` model instantiates."""
        obj = models.Link()
        self.assertTrue(obj, msg='Should instantiate the object')


class LinkCategoryTestCase(TestCase):
    """Tests for the ``LinkCategory`` model class."""
    longMessage = True

    def test_model(self):
        obj = models.LinkCategory()
        self.assertTrue(obj, msg='Should instanciate the object')
