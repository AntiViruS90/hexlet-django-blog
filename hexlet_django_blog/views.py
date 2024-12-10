from django.shortcuts import render


def index(request):
    # context = {'who': 'World'}
    # return render(request, 'index.html', context)
    return render(request, 'base.html')


def about(request):
    tags = ['обучение', 'программирование', 'python', 'ООП']
    return render(
        request,
        'about.html',
        context={'tags': tags}
    )
