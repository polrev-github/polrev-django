import json

from django import template
from django.utils.safestring import mark_safe

from django_redis import get_redis_connection

register = template.Library()

@register.inclusion_tag("reddit/hot.html")
def hot_reddits():
    client = get_redis_connection("default")
    hot = json.loads(client.get('reddit:hot'))
    return {'hot_reddits': hot }
