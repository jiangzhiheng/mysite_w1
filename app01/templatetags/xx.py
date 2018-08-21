#!/usr/bin/env python
#Author:JiangZhiheng

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def f1(value):
    return value + 10



@register.simple_tag
def f2(s1,s2,s3,s4):
    return s1 + s2 + s3 + s4