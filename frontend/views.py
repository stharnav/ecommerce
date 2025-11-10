from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("Hello, welcome to the E-commerce site!")
    return render(request, 'index.html', {'username': 'Ravi'})
