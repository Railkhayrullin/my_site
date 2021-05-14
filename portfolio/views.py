from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm
from .models import MyInfo, MyHobby, PersonalQualities, MySkills, Education, Work, Certifications, Projects, \
    SocialNetwork, ProjectsCategory


def my_site(request):
    context = {
        'my_info': MyInfo.objects.all(),
        'my_hobby': MyHobby.objects.all(),
        'my_personal_qualities': PersonalQualities.objects.all(),
        'my_skills': MySkills.objects.all(),
        'my_education': Education.objects.all(),
        'my_work': Work.objects.all(),
        'my_certifications_education': Certifications.objects.filter(is_education=True),
        'my_certifications': Certifications.objects.filter(is_education=False),
        'my_projects': Projects.objects.all(),
        'my_social_network': MyHobby.objects.all(),
        'projects_category': ProjectsCategory.objects.all(),
        'social_network': SocialNetwork.objects.all()
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            mail = f'Пользователь "{name}" с почтой "{email}"  c сайта-резюме отправил вам сообщение:\n{message}'
            if not settings.DEBUG:
                send_mail('Сообщение с сайта-резюме',
                          mail,
                          settings.SERVER_EMAIL,
                          [get_my_email()],
                          fail_silently=False,)
            else:
                print(mail)
        context['success'] = True
        context['form'] = ContactForm()
    else:
        context['form'] = ContactForm(request.POST)
    return render(request, 'index.html', context)


def get_my_email():
    email = MyInfo.objects.get(pk='1').email
    return email
