from django.shortcuts import render, redirect

def home(request):   
    return render(request, 'shop/home.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')



