from django import template

register = template.Library()

# Ovo gore je bitno inicijalno, dole se kreira funkcija koja ce biti moj filter.
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
