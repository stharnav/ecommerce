from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    return render(request, 'dashboard.html')

def products_page(request):
    return render(request, 'products.html')

def dashboard_page(request):
    return render(request,'dashboard.html')
