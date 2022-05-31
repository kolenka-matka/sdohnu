from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Styles, Artists, Paintings
import random
from .forms import ArtistsForm
from .checking import check
from django.db.models.functions import Lower




def check_answer(style_id, correct_ans, answer):
    # print(correct_ans, " = ", answer)
    if correct_ans == answer:
        ans = "ПРАВИЛЬНЫЙ ОТВЕТ"
    else:
        ans = "ОТВЕТ НЕВЕРЕН"
    return ans



def index(request):
    return render(request, "index.html")
#
def tests(request):
    styles = Styles.objects.all()
    context = {
        'styles': styles
    }
    return render(request, "tests.html", context)

def artists(request):
    artists = Artists.objects.all().order_by(Lower('name'))
    context = {'artists': artists}
    return render(request, "artists.html", context)

def artist_create(request):
    error = ''
    if request.method == 'POST':
        form = ArtistsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artists')
        else:
            error = 'Вы неправильно заполнили форму, мне очень жаль'

    form = ArtistsForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, "artist_create.html", data)

def styles_info(request):
    styles = Styles.objects.all()
    context = {
        'styles': styles
    }
    return render(request, "styles_info.html", context)


def test_game(request):
    # paintings = Paintings.objects.filter(style="2")
    paintings = Paintings.objects.all()
    wrong_ans = []
    for i in paintings:
            answers = random.sample(list(paintings), 3)
            wrong_ans.append(answers)
    # check_answer(1, answers[0], answers[1])
    # print(wrong_ans)
    context = {
        'paintings': paintings,
        'answers': wrong_ans,
    }
    return render(request, "test_game.html", context)

def classicism(request):
    paintings = Paintings.objects.filter(style="1")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/classicism.html", context)

def romantism(request):
    paintings = Paintings.objects.filter(style="2")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/romantism.html", context)


def parsuna(request):
    paintings = Paintings.objects.filter(style="3")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/parsuna.html", context)

def academism(request):
    paintings = Paintings.objects.filter(style="4")
    all_paintings = Paintings.objects.all()
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings,
        'all_paintings': all_paintings
    }
    return render(request, "style_tests/academism.html", context)


def realism(request):
    paintings = Paintings.objects.filter(style="5")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/realism.html", context)

def impressionism(request):
    paintings = Paintings.objects.filter(style="6")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/impressionism.html", context)


def modern(request):
    paintings = Paintings.objects.filter(style="7")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/modern.html", context)

def symbolism(request):
    paintings = Paintings.objects.filter(style="8")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/symbolism.html", context)

def expressionism(request):
    paintings = Paintings.objects.filter(style="9")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/expressionism.html", context)

def postimpressionism(request):
    paintings = Paintings.objects.filter(style="10")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/postimpressionism.html", context)


def cubism(request):
    paintings = Paintings.objects.filter(style="11")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/cubism.html", context)

def avangardism(request):
    paintings = Paintings.objects.filter(style="12")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/avangardism.html", context)


def suprematism(request):
    paintings = Paintings.objects.filter(style="13")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/suprematism.html", context)

def socrealism(request):
    paintings = Paintings.objects.filter(style="14")
    # paintings = Paintings.objects.all()
    context = {
        'paintings': paintings
    }
    return render(request, "style_tests/socrealism.html", context)



