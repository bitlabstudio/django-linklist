"""Factories of the ``linklist`` app."""
import factory

from .. import models


class LinkFactory(factory.Factory):
    FACTORY_FOR = models.Link

    title = 'Test Link'
    url = 'http://www.example.com'


class LinkCategoryFactory(factory.Factory):
    FACTORY_FOR = models.LinkCategory

    name = 'Category'
    slug = 'category'
