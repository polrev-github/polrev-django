from django import template
import us

register = template.Library()

@register.filter(name='fips_title')
def fips_title(fips):
    state = us.states.lookup(fips)
    return state.name

# Pagination support

@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def add(value, arg):
    return value + arg