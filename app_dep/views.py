from django.shortcuts import render,  HttpResponse


def home(request) -> HttpResponse:
    '''
    Home
    '''
    return render(request, 'home.html')
