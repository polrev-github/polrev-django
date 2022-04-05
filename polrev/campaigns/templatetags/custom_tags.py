from django import template
import us

register = template.Library()

@register.filter(name='fips_title')
def fips_title(fips):
    state = us.states.lookup(fips)
    return state.name