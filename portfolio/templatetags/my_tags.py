from django import template
from portfolio.models import MyHobby, PersonalQualities, MySkills, Education, Work, Certifications, Projects, \
    SocialNetwork

register = template.Library()


@register.simple_tag()
def get_my_hobby():
    return MyHobby.objects.all()


@register.filter(name='split')
def slpit_filter(value, arg):
    return value.split(arg)
