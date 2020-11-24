from django import template

register=template.Library()

def cuslower(value):
    result=value[:3].lower()
    return  result
register.filter('mylower',cuslower)


@register.filter(name='myappend')
def append(value,arg):
    result=str(arg)+value
    return  result

