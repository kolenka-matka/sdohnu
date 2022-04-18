from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")
#
def tests(request):
    return render(request, "tests.html")

def artists(request):
    return render(request, "artists.html")

def styles_info(request):
    return render(request, "styles_info.html")