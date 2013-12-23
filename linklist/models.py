"""Models for the ``linklist`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField


class LinkCategory(models.Model):
    """
    Category for a link.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug'),
        blank=True,
    )

    def __unicode__(self):
        return self.name


class Link(models.Model):
    """
    Contains an URL and link-related data.

    :category: Optional category for this link
    :title: Title of the link.
    :url: URL of the link.
    :image: Screenshot of the link.
    :description: Long description of the link.
    :position: Position of the object. Can be used for ordering.
    :alignment: Choices to render the link left or right aligned.

    """
    category = models.ForeignKey(
        'LinkCategory',
        verbose_name=_('Link category'),
        related_name='links',
        null=True, blank=True,
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=256,
    )

    url = models.URLField(
        verbose_name=_('URL'),
        max_length=2048,
    )

    image = FilerImageField(
        verbose_name=_('Image'),
        related_name='link_images',
        null=True, blank=True,
    )

    description = models.TextField(
        verbose_name=_('Description'),
        max_length=4000,
        blank=True,
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        blank=True, null=True,
    )

    alignment = models.CharField(
        verbose_name=_('Alignment'),
        max_length=10,
        choices=(
            ('left', 'left'),
            ('right', 'right'),
            ('center', 'center'),
        ),
        default='left',
    )

    class Meta:
        ordering = ['position', ]

    def __unicode__(self):
        return '{0}'.format(self.title)
