"""Templatetags for the linklist app."""
import operator

from django import template
from django.db.models import Q

from .. import models


register = template.Library()


@register.assignment_tag
def get_linklist(amount=4, categories=None):
    qs = models.Link.objects.all()
    if categories:
        categories_list = categories.split(',')
        qlist = None
        for category in categories_list:
            if qlist is None:
                qlist = Q(category__slug=category)
            else:
                qlist = qlist | Q(category__slug=category)
        qs = qs.filter(qlist)
    return qs[:amount]
