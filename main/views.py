from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import AlatOlahraga, Rating, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import reverse 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserLoginForm, AlatOlahragaForm, RatingForm, ReviewForm
import datetime
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
import datetime

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role', 'user')
            user.save()
            messages.success(request, 'Your account has been successfully created!')
            login(request, user)  # Loginkan user setelah registrasi
            
            # Redirect ke halaman utama
            response = redirect('main:show_main')  # pastikan ini sesuai dengan nama di urls.py
            response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return response

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')  # Redirect after successful login
        else:
            messages.error(request, "Login failed. Please check your credentials.")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

@login_required(login_url="/login/")
def show_main(request):
    print("Accessing show_main view")  # Ini akan muncul di konsol jika view ini terakses
    context = {
        'username': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'main.html', context)


def rate_product(request, alat_id):
    alat = get_object_or_404(AlatOlahraga, id=alat_id)
    rating, created = Rating.objects.get_or_create(alat_olahraga=alat, user=request.user)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('product_detail', alat_id=alat.id)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'rate_product.html', {'form': form, 'alat': alat})

def review_product(request, alat_id):
    alat = get_object_or_404(AlatOlahraga, id=alat_id)
    review, created = Review.objects.get_or_create(alat_olahraga=alat, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_detail', alat_id=alat.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_product.html', {'form': form, 'alat': alat})

from django.shortcuts import render, get_object_or_404, redirect
from .models import AlatOlahraga, Rating, Review
from .forms import RatingForm, ReviewForm
from django.contrib.auth.decorators import login_required

@login_required
def user_reviews_and_ratings(request):
    user_ratings = Rating.objects.filter(user=request.user)
    user_reviews = Review.objects.filter(user=request.user)
    rating_form = RatingForm()
    review_form = ReviewForm()

    # Cek jika request method adalah POST untuk menambah rating atau review
    if request.method == "POST":
        if 'submit_rating' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.user = request.user
                rating.alat_olahraga = get_object_or_404(AlatOlahraga, id=request.POST.get('alat_olahraga'))
                rating.save()
                return redirect('main:user_reviews_and_ratings')
        
        elif 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.alat_olahraga = get_object_or_404(AlatOlahraga, id=request.POST.get('alat_olahraga'))
                review.save()
                return redirect('main:user_reviews_and_ratings')

    context = {
        'user_ratings': user_ratings,
        'user_reviews': user_reviews,
        'rating_form': rating_form,
        'review_form': review_form,
        'alat_olahraga_list': AlatOlahraga.objects.all(),
    }
    return render(request, 'user_reviews_and_ratings.html', context)

  
def create_rating(request, alat_id):
    alat = get_object_or_404(AlatOlahraga, pk=alat_id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        comment = request.POST.get('comment')
        rating, created = Rating.objects.update_or_create(
            alat_olahraga=alat, user=request.user,
            defaults={'rating': rating_value, 'comment': comment}
        )
        alat.update_rating()  # Update the average rating
        return redirect('alat_detail', alat_id=alat.id)
    return render(request, 'ratings/create_rating.html', {'alat': alat})

def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id, user=request.user)
    alat = rating.alat_olahraga
    rating.delete()
    alat.update_rating()  # Update the average rating after deletion
    return redirect('alat_detail', alat_id=alat.id)

def create_review(request, alat_id):
    alat = get_object_or_404(AlatOlahraga, pk=alat_id)
    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        rating_value = request.POST.get('rating')
        review, created = Review.objects.update_or_create(
            alat_olahraga=alat, user=request.user,
            defaults={'review_text': review_text, 'rating': rating_value}
        )
        alat.update_rating()  # Update the average rating based on new review
        return redirect('alat_detail', alat_id=alat.id)
    return render(request, 'reviews/create_review.html', {'alat': alat})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    alat = review.alat_olahraga
    review.delete()
    alat.update_rating()  # Update the average rating after deletion
    return redirect('alat_detail', alat_id=alat.id)

def get_rating(request, product_id):
    product = get_object_or_404(AlatOlahraga, id=product_id)
    ratings = product.ratings.all()
    average_rating = ratings.aggregate(models.Avg('rating'))['rating__avg'] or 0
    return JsonResponse({'average_rating': average_rating})

def get_reviews(request, product_id):
    product = get_object_or_404(AlatOlahraga, id=product_id)
    reviews = list(product.reviews.values('user__username', 'review'))
    return JsonResponse({'reviews': reviews})

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

def create_alat(request):
    if request.method == "POST":
        form = AlatOlahragaForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to the database
            return redirect('main:alat_list')
    else:
        form = AlatOlahragaForm()  # Create a new empty form for GET requests
    return render(request, 'create_alat.html', {'form': form})  # Render the form in the template

# Read
def alat_list(request):
    alat_items = AlatOlahraga.objects.all()
    paginator = Paginator(alat_items, 10)  # Show 10 items per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'alat_list.html', {'page_obj': page_obj})

def alat_detail(request, pk):
    alat = get_object_or_404(AlatOlahraga, pk=pk)
    return render(request, 'alat_detail.html', {'alat': alat})

def delete_alat(request, id):
    alat = get_object_or_404(AlatOlahraga, id=id)
    if request.method == 'POST':
        alat.delete()
    return redirect('main:alat_list')
   
def rating_list(request):
    ratings = Rating.objects.all().order_by('-id')  # Order by latest
    paginator = Paginator(ratings, 10)  # 10 ratings per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'rating_list.html', context)

def rating_delete(request, id):
    rating = get_object_or_404(Rating, id=id) 
    if request.method == 'POST': 
        rating.delete()  # Delete the rating
        return redirect('main:rating_list')

def review_list(request):
    reviews = Review.objects.all()  
    paginator = Paginator(reviews, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'review_list.html', {'page_obj': page_obj})

@login_required
def rating_create(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user  # Set to the logged-in CustomUser instance
            rating.save()
            return redirect('main:rating_list')
    else:
        form = RatingForm()
        
    context = {
        'form': form,
        'alat_olahraga_list': AlatOlahraga.objects.all()  # Pass the list of Alat Olahraga items to the template
    }
    return render(request, 'rating_create.html', context)

def rating_edit(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('main:rating_list')
    else:
        form = RatingForm(instance=rating)
    context = {
        'form': form,
        'alat_olahraga_list': AlatOlahraga.objects.all()
    }
    return render(request, 'rating_edit.html', context)

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('main:review_list')
    else:
        form = ReviewForm()
    context = {
        'form': form,
        'alat_olahraga_list': AlatOlahraga.objects.all() 
    }
    return render(request, 'review_create.html', context)

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('main:review_list')
    else:
        # Initialize the form for GET requests
        form = ReviewForm(instance=review)

    # Context includes both the form and the list of sports equipment
    context = {
        'form': form,
        'alat_olahraga_list': AlatOlahraga.objects.all()  # Include the list here
    }

    return render(request, 'review_edit.html', context)


def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('main:review_list')
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})
# Update
def edit_alat(request, id):
    alat = get_object_or_404(AlatOlahraga, id=id)
    if request.method == 'POST':
        form = AlatOlahragaForm(request.POST, instance=alat)
        if form.is_valid():
            form.save()
            return redirect('main:alat_list')
    else:
        form = AlatOlahragaForm(instance=alat)
    return render(request, 'edit_alat.html', {'form': form})

def get_article_details(request, article_id): 
    articles = {
        1: {
            "id": 1,
            "title": "Berstandar Internasional, Jakarta Running Festival 2024 Manjakan Para Peserta",
            "image_url": "/static/image/article1.jpg",
            "short_description": "Ajang marathon berstandar internasional, Jakarta Running Festival (JRF) 2024...",
        },
        2: {
            "id": 2,
            "title": "Soft tennis - Permainan solid bawa beregu putri Jakarta dulang emas",
            "image_url": "/static/image/article2.jpg",
            "short_description": "DKI Jakarta sukses mendulang medali emas cabang olahraga soft tenis beregu putri...",
        },
        3: {
            "id": 3,
            "title": "7 Lapangan Golf Terbaik di Jakarta, Fasilitas dan Biayanya",
            "image_url": "/static/image/article3.jpg",
            "short_description": "Salah satu lapangan golf di Jakarta dalam daftar ini dianggap sebagai lapangan kelas...",
        },
        4: {
            "id": 4,
            "title": "Menpora ajak masyarakat turut serta dalam Festival Yoga di Jakarta",
            "image_url": "/static/image/article4.jpg",
            "short_description": "Menteri Pemuda dan Olahraga Dito Ariotedjo mengajak masyarakat turut serta dalam...",
        },

        5: {
            "id": 5,
            "title": "Cerita Royke Lumowa Bersepeda Setahun dari Jakarta ke Paris Demi Dukung Indonesia di Olimpiade 2024",
            "image_url": "/static/image/article5.jpg",
            "short_description": "Mantan Dirlantas Polda Metro Jaya Irjen Pol (Purn) Royke Lumowa memberikan dukungan kepada...",
        },

        6: {
            "id": 6,
            "title": "Indonesia Vs Bahrain di GBK Masih Tanda Tanya",
            "image_url": "/static/image/article5.jpg",
            "short_description": "Menpora Dito Ariotedjo menyebut FIFA sudah memutuskan laga Timnas Indonesia vs...",
        },
    }
    
    article = articles.get(article_id)
    
    if article:
        return JsonResponse(article)
    else:
        return JsonResponse({'error': 'Article not found'}, status=404)