
# copy the codes from : in google search django template tags
# then search "simple" keyword and copy them

from django import template

register = template.Library()

@register.simple_tag
def title(data='وبلاگ جنگویی'):
    return data

# copy the codes from : in google search django template tags
# then search "simple" keyword and copy them
from ..models import Category
@register.inclusion_tag('first_app/partials/category_navbar.html')
def category_navbar():
    return {
        'category': Category.objects.filter(status=True)
    }


@register.inclusion_tag("registration/partials/link.html")
def link(request , link_name , content , classes):
    return {
        "request":request ,
        "link_name":link_name ,
        "link" : "account:{}".format(link_name),
        "content":content,
        "classes": classes,

    }