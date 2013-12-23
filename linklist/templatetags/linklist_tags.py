"""Templatetags for the linklist app."""
from django import template

from .. import models


register = template.Library()


@register.assignment_tag
def get_linklist(amount=4, category=None):
    qs = models.Link.objects.all()
    if category:
        qs = qs.filter(category__slug__iexact=category)
    return qs[:amount]
