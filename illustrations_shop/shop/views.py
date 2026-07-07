from django.shortcuts import render, redirect

def home(request):   
    return render(request, 'shop/home.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def products(request):
    return render(request, 'shop/products.html')

def product(request):
    return render(request, 'shop/product.html')

def illustrations(request):
    return render(request, 'shop/illustrations.html')

def individual_illustrations(request):
    return render(request, 'shop/individual_illustrations.html')

def illustration_packages(request):
    return render(request, 'shop/illustration_packages.html')

def icons(request):
    return render(request, 'shop/icons.html')

def icon_sets(request):
    return render(request, 'shop/icon_sets.html')

def individual_icons(request):
    return render(request, 'shop/individual_icons.html')

def basket(request):
    return render(request, 'shop/basket.html')

def privacy(request):
    return render(request, 'shop/privacy.html')

def conditions(request):
    return render(request, 'shop/conditions.html')






