from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
        This cuts out all values of "arg" from string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
# we created templattags(folder) & __init__.py and my_extras.py by ourself
