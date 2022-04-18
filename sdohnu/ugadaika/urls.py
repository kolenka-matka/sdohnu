from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # путь к главной странице сайта
    path('tests/', views.tests, name='tests'),
    path('artists/', views.artists, name='artists'),
    path('styles_info/', views.styles_info, name='styles_info'),
]