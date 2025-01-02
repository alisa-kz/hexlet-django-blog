from django.shortcuts import render, redirect
from django.views import View
# from django.http import HttpResponse


# def index(request):
#     name = 'article'
#     return render(
#         request,
#         'articles_index.html',
#         context={'name': name}
#     )

class IndexView(View):

    def get(self, request, tags=None, article_id=None):
        article_dict = {'tags': tags, 'article_id': article_id}
        return render(
            request,
            'articles_index.html',
            context={'article_dict': article_dict}
        )
