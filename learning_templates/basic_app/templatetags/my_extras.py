from django import template

register = template.Library()

def cut(value,arg):
    """
    docstring
    """
    return value.replace(arg,'')

register.filter("cut",cut)
