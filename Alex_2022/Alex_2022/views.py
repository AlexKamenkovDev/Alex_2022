from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def reverse(request):
    # user_text = request.GET['username']
    # reversed_text = user_text[::-1]
    return render(request, 'reverse.html')


def home(request):
    return HttpResponse('This is my homepage.')
