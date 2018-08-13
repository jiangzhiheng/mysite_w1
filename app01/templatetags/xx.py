#!/usr/bin/env python
#Author:JiangZhiheng

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def f1(value):
    return value + 10