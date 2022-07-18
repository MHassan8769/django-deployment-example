from django import template

register = template.Library()
@register.filter(name = 'cut')
def cut(value,arg):
    """"
    this cut all values od "arg" from the string

    """

    return value.replace(arg,'')
