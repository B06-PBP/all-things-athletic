# main/views.py
# main/views.py

# from models import Product

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})

from django.shortcuts import render
from .models import AlatOlahraga

def show_main(request):
    # Mengambil data dari database
    data_alat_olahraga = AlatOlahraga.objects.all()

    # Memproses toko menjadi list di views.py
    for product in data_alat_olahraga:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_alat_olahraga
    }
    
    return render(request, 'main.html', context)


