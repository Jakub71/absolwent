from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>witaj w Django!</h1>")

def test(request):
    return HttpResponse("To tylko test")