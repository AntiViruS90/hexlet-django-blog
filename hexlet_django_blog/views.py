from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'base.html'


def about(request):
    tags = ['обучение', 'программирование', 'python', 'ООП']
    return render(
        request,
        'about.html',
        context={'tags': tags}
    )
