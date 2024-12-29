from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    name = 'article'
    return render(
        request,
        'articles_index.html',
        context={'name': name}
    )
