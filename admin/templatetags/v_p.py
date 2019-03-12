from django import template

register = template.Library()

@register.filter
def v_p(value):
    value = str(value)
    return value.replace(",",".")