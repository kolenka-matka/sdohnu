from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # путь к главной странице сайта
    path('tests/', views.tests, name='tests'),
    path('artists/', views.artists, name='artists'),
    path('styles_info/', views.styles_info, name='styles_info'),
    path('tests/play', views.styles_info, name='play'),
    path('artists/create', views.artist_create, name='artist_create'),

    path('tests/классицизм', views.classicism, name='классицизм'),
    path('tests/романтизм', views.romantism, name='романтизм'),
    path('tests/парсуна', views.parsuna, name='парсуна'),
    path('tests/академизм', views.academism, name='академизм'),
    path('tests/реализм', views.realism, name='реализм'),
    path('tests/импрессионизм', views.impressionism, name='импрессионизм'),
    path('tests/модерн', views.modern, name='модерн'),
    path('tests/символизм', views.symbolism, name='символизм'),
    path('tests/экспрессионизм', views.expressionism, name='экспрессионизм'),
    path('tests/постимпрессионизм', views.postimpressionism, name='постимпрессионизм'),
    path('tests/кубизм', views.cubism, name='кубизм'),
    path('tests/авангардизм', views.avangardism, name='авангардизм'),
    path('tests/супрематизм', views.suprematism, name='супрематизм'),
    path('tests/соцреализм', views.socrealism, name='соцреализм'),
]