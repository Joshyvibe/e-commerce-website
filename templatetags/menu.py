from django import template
from store.models import Category



register = template.Library()

@register.inclusion_tag('online_site/menu.html')

def menu():
    categories = Category.objects.all()
    return {'categories': categories}