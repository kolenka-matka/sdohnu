"""sdohnu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ugadaika import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('tests/', views.tests, name='tests'),
    path('artists/', views.artists, name='artists'),
    path('styles_info/', views.styles_info, name='styles_info'),
    path('tests/play', views.test_game, name='play'),
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
    # path(r'^login/$', views.user_login, name='login'),
]
