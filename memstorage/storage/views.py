from django.shortcuts import render

from .models import mem

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    mems=mem.objects.all().order_by('-date')

    return render(
        request,
        'index.html',
        context={'mems':mems},
    )