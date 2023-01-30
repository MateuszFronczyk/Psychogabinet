from django.shortcuts import render

def main_page(request):
    return render(request, 'm_info_specjalista.html')

def cennik_page(request):
    return render(request, 'cennik.html')

def czat_page(request):
    return render(request, 'czat_specjalista.html')

def kalendarz_page(request):
    return render(request, 'kalendarz.html')

def pacjenci_page(request):
    return render(request, 'pacjenci_specjalista.html')

def wizyty_page(request):
    return render(request, 'wizyty.html')