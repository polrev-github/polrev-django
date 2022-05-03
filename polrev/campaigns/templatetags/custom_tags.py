from django import template
from django.utils.safestring import mark_safe

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

@register.simple_tag(takes_context=True)
def pager(context):
    campaigns = context['campaigns']
    page_number = campaigns.number
    paginator = campaigns.paginator
    num_pages = paginator.num_pages
    
    width = 4
    half_width = int(width / 2)
    first = page_number - half_width
    first = 1 if first < 1 else first
    last = first + width
    last = num_pages + 1 if last > num_pages else last
    window = range(first, last)

    if not campaigns:
        return mark_safe('<p>No items found.</p>\n')
    elif num_pages == 1:
        return ''

    lines = ["""
    <nav aria-label="Item pagination">
      <ul class="pagination">
    """]

    if campaigns.has_previous():
        lines.append(f"""
        <li class="page-item">
        <a class="page-link" href="?page={campaigns.previous_page_number()}" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
        </a>
        </li>
        """)

    if first > 2:
        lines.append(f"""
        <li class="page-item">
            <a class="page-link" href="?page=1">
                1
            </a>
        </li>
        <li class="page-item">
            <span class="page-link">{paginator.ELLIPSIS}</span>
        </li>
        """)

    for i in window:
        active = 'active' if i == page_number else None
        lines.append(f"""
        <li class="page-item {active}">
            <a class="page-link" href="?page={i}">
                {i}
            </a>
        </li>
        """)

    if page_number < num_pages - half_width:
        lines.append(f"""
        <li class="page-item">
            <span class="page-link">{paginator.ELLIPSIS}</span>
        </li>
        <li class="page-item">
            <a class="page-link" href="?page={num_pages}">
                {num_pages}
            </a>
        </li>
        """)

    if campaigns.has_next():
        lines.append(f"""
        <li class="page-item">
        <a class="page-link" href="?page={campaigns.next_page_number()}" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
        </a>
        </li>  
        """)

    lines.append("</ul></nav>")

    return mark_safe("\n".join(lines))