from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from main_app.models import Greeting


def index(request):
    return HttpResponse("Hello, world!")


def page2(request):
    return render(request, "page2.html")


def page3_view(request):
    all_greetings = Greeting.objects.all() # will be written to all_greetings: QuerySet
    return render(request, "page3.html", context={"data": all_greetings})


def page4_view(request):
    greetings_dict = []
    for elem in Greeting.objects.all():
        greetings_dict.append(f'lang: {elem.language}, text: {elem.text}\n')
    return render(request, "page4.html", context={"data2": greetings_dict})
