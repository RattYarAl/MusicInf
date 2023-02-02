from django import template

register = template.Library()


@register.filter(name='split')
def split(value):
    return value.split('\r\n')


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
