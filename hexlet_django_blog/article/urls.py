from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    # path('', views.index),
    path('', views.IndexView.as_view(), name='article_index'),
    path('<int:id>/', views.ArticleView.as_view(), name='article')
]
