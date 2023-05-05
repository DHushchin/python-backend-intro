from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aircraft(request):
    return render(request, 'aircraft.html')

def price(request):
    return render(request, 'price.html')

def contacts(request):
    return render(request, 'contacts.html')
