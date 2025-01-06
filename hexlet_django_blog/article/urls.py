from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    # path('', views.index),
    path("", views.IndexView.as_view(), name="article_index"),
    path("<int:id>/edit/", views.ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/delete/", views.ArticleFormDeleteView.as_view(), name="articles_delete"),
    path("<int:id>/", views.ArticleView.as_view(), name="article"),
    path("create/", views.ArticleFormCreateView.as_view(), name="articles_create"),
]
