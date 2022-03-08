from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # путь к главной странице сайта
]