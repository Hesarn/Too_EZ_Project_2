from django import template
import datetime
from math import ceil, floor
register = template.Library()

@register.filter(name='age')
def age(birthday_year):
    return datetime.datetime.now().year - birthday_year

@register.filter(name='round')
def round(num):
    if num-int(num) > 0.5:
        return ceil(num)
    else:
        return floor(num)
