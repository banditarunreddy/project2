from django.shortcuts import render
from django .http import HttpResponse

def first(request):
    return HttpResponse('I AM TARUN')
