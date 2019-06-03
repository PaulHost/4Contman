from django.conf.urls import url

from word_searcher import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
