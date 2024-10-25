from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import AlatOlahraga
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import reverse 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

@login_required(login_url="/login")
def show_main(request):
    context = {
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'main.html', context)

def show_articles(request):
    return render(request, "articles.html")

def show_article1(request):
    return render(request, "article1.html")

def show_article2(request):
    return render(request, "article2.html")

def show_article3(request):
    return render(request, "article3.html")

def show_article4(request):
    return render(request, "article4.html")

def show_article5(request):
    return render(request, "article5.html")

def show_article6(request):
    return render(request, "article6.html")

def show_product(request):
    # Mengambil data dari database
    data_alat_olahraga = AlatOlahraga.objects.all()

    # Memproses toko menjadi list di views.py
    for product in data_alat_olahraga:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_alat_olahraga
    }
    
    return render(request, 'product.html', context)

def show_yoga(request):
    # Mengambil data dari database yang hanya memiliki kategori 'yoga'
    data_yoga = AlatOlahraga.objects.filter(cabang_olahraga='Yoga')

    # Memproses toko menjadi list di views.py
    for product in data_yoga:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_yoga
    }
    
    return render(request, 'product.html', context)

def show_cycling(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Cycling'
    data_cycling = AlatOlahraga.objects.filter(cabang_olahraga='Cycling')

    # Memproses toko menjadi list di views.py
    for product in data_cycling:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_cycling
    }
    
    return render(request, 'product.html', context)

def show_tennis(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Tennis'
    data_tennis = AlatOlahraga.objects.filter(cabang_olahraga='Tennis')

    # Memproses toko menjadi list di views.py
    for product in data_tennis:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_tennis
    }
    
    return render(request, 'product.html', context)

def show_boxing(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Boxing'
    data_boxing = AlatOlahraga.objects.filter(cabang_olahraga='Boxing')

    # Memproses toko menjadi list di views.py
    for product in data_boxing:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_boxing
    }
    
    return render(request, 'product.html', context)

def show_badminton(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Badminton'
    data_badminton = AlatOlahraga.objects.filter(cabang_olahraga='Badminton')

    # Memproses toko menjadi list di views.py
    for product in data_badminton:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_badminton
    }
    
    return render(request, 'product.html', context)

def show_basketball(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Basketball'
    data_basketball = AlatOlahraga.objects.filter(cabang_olahraga='Basketball')

    # Memproses toko menjadi list di views.py
    for product in data_basketball:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_basketball
    }
    
    return render(request, 'product.html', context)

def show_running(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Running'
    data_running = AlatOlahraga.objects.filter(cabang_olahraga='Running')

    # Memproses toko menjadi list di views.py
    for product in data_running:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_running
    }
    
    return render(request, 'product.html', context)

def show_football(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Football'
    data_football = AlatOlahraga.objects.filter(cabang_olahraga='Football')

    # Memproses toko menjadi list di views.py
    for product in data_football:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_football
    }
    
    return render(request, 'product.html', context)

def show_swimming(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Swimming'
    data_swimming = AlatOlahraga.objects.filter(cabang_olahraga='Swimming')

    # Memproses toko menjadi list di views.py
    for product in data_swimming:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_swimming
    }
    
    return render(request, 'product.html', context)

def show_golf(request):
    # Mengambil data dari database yang hanya memiliki kategori 'Golf'
    data_golf = AlatOlahraga.objects.filter(cabang_olahraga='Golf')

    # Memproses toko menjadi list di views.py
    for product in data_golf:
        product.toko_list = product.toko.split(', ')  # Membuat list dari toko yang dipisahkan koma

    context = {
        'data_alat_olahraga': data_golf
    }
    
    return render(request, 'product.html', context)

def get_article_details(request, article_id): 
    articles = {
        1: {
            "id": 1,
            "title": "Berstandar Internasional, Jakarta Running Festival 2024 Manjakan Para Peserta",
            "image_url": "/static/image/article1.jpg",
            "short_description": "Ajang marathon berstandar internasional, Jakarta Running Festival (JRF) 2024 resmi dibuka pada Kamis (10/10/2024) di Istora Senayan, Jakarta. Pada gelaran tahun ini, para peserta dimanjakan dengan sejumlah...",
        },
        2: {
            "id": 2,
            "title": "Soft tennis - Permainan solid bawa beregu putri Jakarta dulang emas",
            "image_url": "/static/image/article2.jpg",
            "short_description": "DKI Jakarta sukses mendulang medali emas cabang olahraga soft tenis beregu putri Pekan Olahraga Nasional (PON) XXI Aceh-Sumatera Utara 2024 berkat permainan yang solid saat...",
        },
        3: {
            "id": 3,
            "title": "7 Lapangan Golf Terbaik di Jakarta, Fasilitas dan Biayanya",
            "image_url": "/static/image/article3.jpg",
            "short_description": "Golf sudah hadir sejak lama di Indonesia, yaitu dari tahun 1872. Namun, olahraga ini tidak sepopuler sepak bola atau bulu tangkis. Salah satu alasan utamanya adalah anggapan bahwa golf...",
        },
        4: {
            "id": 4,
            "title": "Menpora ajak masyarakat turut serta dalam Festival Yoga di Jakarta",
            "image_url": "/static/image/article4.jpg",
            "short_description": "Menteri Pemuda dan Olahraga Dito Ariotedjo mengajak masyarakat turut serta dalam Festival Yoga yang digelar di Jakarta oleh Isha Foundation dan bertepatan dengan...",
        },

        5: {
            "id": 5,
            "title": "Cerita Royke Lumowa Bersepeda Setahun dari Jakarta ke Paris Demi Dukung Indonesia di Olimpiade 2024",
            "image_url": "/static/image/article5.jpg",
            "short_description": "Mantan Dirlantas Polda Metro Jaya Irjen Pol (Purn) Royke Lumowa memberikan dukungan kepada kontingen Indonesia di Olimpiade 2024 dengan cara unik dan spesial. Royke bersepeda dari Jakarta ke Paris sekitar setahun...",
        },

        6: {
            "id": 6,
            "title": "Indonesia Vs Bahrain di GBK Masih Tanda Tanya",
            "image_url": "/static/image/article5.jpg",
            "short_description": "Menpora Dito Ariotedjo menyebut FIFA sudah memutuskan laga Timnas Indonesia vs Bahrain akan tetap..",
        },
    }
    
    article = articles.get(article_id)
    
    if article:
        return JsonResponse(article)
    else:
        return JsonResponse({'error': 'Article not found'}, status=404)