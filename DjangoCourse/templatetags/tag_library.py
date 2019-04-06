from django import template

register = template.Library()

@register.filter()
def to_float(value):
    return float(value)

