from django import template

register = template.Library()

"""
This fn cuts out all the values of arg from the string
"""
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg,'')

# register.filter('cut',cut)
