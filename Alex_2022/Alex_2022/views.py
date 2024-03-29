from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 5 + 6
    return render(request, 'about.html', {'greeting': a})


def reverse(request):
    user_text = request.GET['username']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'word': reversed_text})


def home(request):
    return HttpResponse('This is my homepage.')
