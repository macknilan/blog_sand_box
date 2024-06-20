import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def render_markdown(value):
    return markdown.markdown(
        value,
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc",
        ],
    )
