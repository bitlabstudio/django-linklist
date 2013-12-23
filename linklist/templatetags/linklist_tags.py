"""Templatetags for the linklist app."""
from django import template

from .. import models


register = template.Library()


@register.assignment_tag
def get_linklist(amount=4):
    return models.Link.objects.all()[:amount]
