from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='upcase_first_letter')
def upcase_first_letter(value):
    return value.capitalize()
