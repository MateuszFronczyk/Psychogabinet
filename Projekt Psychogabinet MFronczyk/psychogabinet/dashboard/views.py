from django.shortcuts import render

def login_page(request):
    return render(request, 'login-page.html')

def register_page(request):
    return render(request, 'rejestracja.html')