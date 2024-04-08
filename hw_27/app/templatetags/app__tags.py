from django import template
import datetime
register=template.Library()
@register.filter(name='curreny')
def render_curreny(value):
    return " {:,.2f}".format(value)
@register.filter(name='upper')
def upper(value):
    return value.upper()
@register.simple_tag(name="greeting")
def greeting(name):
    return f"Hello, {name}!"


@register.simple_tag(name="greeting2")
def greeting2():
   
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
        return "Good morning!"
    elif 12 <= now.hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"