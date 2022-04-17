from django import template

register = template.Library()


@register.filter
def notifilter(args):
    filtered = []
    for i in args:
        if i.read is False:
            filtered.append(i)
    return 