from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import AlatOlahraga, Article, CommentRatingArticle, Rating, Review, CustomUser
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
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def register(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role', 'user')  # Set role to 'user' by default
            user.save()
            messages.success(request, 'Your account has been successfully created!')
            login(request, user)  # Automatically log in the user after registration
            return redirect('main:show_main')  # Adjust to redirect after registration

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

@login_required(login_url="/login")
def show_main(request):
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

def user_reviews_and_ratings(request):
    user_ratings = Rating.objects.filter(user=request.user)
    user_reviews = Review.objects.filter(user=request.user)
    rating_form = RatingForm()
    review_form = ReviewForm()

    context = {
        'user_ratings': user_ratings,
        'user_reviews': user_reviews,
        'rating_form': rating_form,
        'review_form': review_form,
        'alat_olahraga_list': AlatOlahraga.objects.all(),  # Include the list here
    }
    return render(request, 'user_reviews_and_ratings.html', context)

def user_ratings_flutter(request, id):
    user_ratings = Rating.objects.filter(user_id=id)

    return HttpResponse(serializers.serialize("json", user_ratings), content_type="application/json")
  
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

def rating_delete(request, pk):
    rating = get_object_or_404(Rating, id=pk) 
    if request.method == 'POST': 
        rating.delete()  # Delete the rating
        return redirect('main:rating_list')

def review_list(request):
    reviews = Review.objects.all()  
    paginator = Paginator(reviews, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'review_list.html', {'page_obj': page_obj})

from django.db import IntegrityError

from django.db import IntegrityError

@login_required
def rating_create(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)  # Temporarily save the form data without committing to the database
            rating.user = request.user  # Associate the rating with the logged-in user

            # Retrieve the AlatOlahraga ID from the form data
            alat_olahraga_id = request.POST.get('alat_olahraga')

            try:
                # Check if the AlatOlahraga object exists
                alat = AlatOlahraga.objects.get(id=alat_olahraga_id)
                rating.alat_olahraga = alat  # Link the rating to the AlatOlahraga object
                
                # Save the rating to the database
                rating.save()
                return redirect('main:rating_list')  # Redirect to the rating list page

            except AlatOlahraga.DoesNotExist:
                # If AlatOlahraga does not exist, add an error message to the form
                form.add_error('alat_olahraga', 'The selected Alat Olahraga does not exist.')

            except IntegrityError as e:
                # Catch and log the IntegrityError if a foreign key constraint fails
                form.add_error(None, 'An error occurred while saving the rating. Please try again.')

        else:
            # Print form errors for debugging if the form is invalid
            print(form.errors)
    else:
        form = RatingForm()  # Initialize a new form if the request is GET

    context = {
        'form': form,
        'alat_olahraga_list': AlatOlahraga.objects.all()  # Populate the dropdown with all AlatOlahraga options
    }
    return render(request, 'rating_create.html', context)  # Render the form with the context


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
            review = form.save(commit=False)  # Save without committing to database
            review.user = request.user  # Associate the review with the logged-in user

            # Retrieve the AlatOlahraga ID from form data
            alat_olahraga_id = request.POST.get('alat_olahraga')
            try:
                # Ensure the AlatOlahraga instance exists
                alat = AlatOlahraga.objects.get(id=alat_olahraga_id)
                review.alat_olahraga = alat  # Link the review to the AlatOlahraga object
                
                # Save the review to the database
                review.save()
                return redirect('main:review_list')  # Redirect to the review list page

            except AlatOlahraga.DoesNotExist:
                form.add_error('alat_olahraga', 'The selected Alat Olahraga does not exist.')

            except IntegrityError as e:
                form.add_error(None, 'An error occurred while saving the review. Please try again.')

        else:
            print("Form validation errors:", form.errors)

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'alat_olahraga_list': AlatOlahraga.objects.all()  # Populate dropdown with AlatOlahraga options
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
    
def show_alat_olahraga_json(request):
    data = AlatOlahraga.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_article_json(request):
    data = Article.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_article_commrat(request, pk):
    data = CommentRatingArticle.objects.filter(article_id = pk)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_rating_list_json(request):
    data = Rating.objects.all().order_by('-id')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_review_list_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_username(request, id):
    try:
        user = CustomUser.objects.get(id=id)
        return JsonResponse({"username": user.username})
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    
def get_alat(request, id):
    try:
        alat = AlatOlahraga.objects.get(id=id)
        return JsonResponse({"nama_alat": alat.alat_olahraga})
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

@csrf_exempt
def create_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        alat_olahraga_id = data['alat_olahraga']
        rating = data['rating']
        review = data['review']

        if not all([alat_olahraga_id, rating, review]):
            return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)
        
        try:
            alat = AlatOlahraga.objects.get(id=alat_olahraga_id)
        except AlatOlahraga.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Alat Olahraga does not exist"}, status=400)
        
        # Buat objek Review

        review = Review.objects.create(
            user=request.user,
            alat_olahraga=alat,
            rating=float(rating),
            review_text=review
        )
        
        review.save()
        
        return JsonResponse({"status": "success", "review_id": str(review.id)}, status=201)
       
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
@csrf_exempt
@require_http_methods(["GET", "POST"])
def edit_review_flutter(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)

    if request.method == 'GET':
        alat_list = AlatOlahraga.objects.all()
        data = {
            "status": "success",
            "review": {
                "id": review.pk,
                "alat_olahraga_pk": review.alat_olahraga.pk,
                "review_text": review.review_text,
                "rating": review.rating,
            },
            "alat_olahraga_list": [
                {
                    "pk": alat.pk,
                    "alat_olahraga": alat.alat_olahraga,
                }
                for alat in alat_list
            ]
        }
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        
        data = json.loads(request.body)
        alat_olahraga_pk = data['alat_olahraga']
        review_text = data['review_text']
        rating = data['rating']

        if not all([alat_olahraga_pk, review_text, rating is not None]):
            return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)

        try:
            alat = AlatOlahraga.objects.get(pk=alat_olahraga_pk)
        except AlatOlahraga.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Alat Olahraga does not exist"}, status=400)

        try:
            rating = float(rating)
            if rating < 0 or rating > 5:
                return JsonResponse({"status": "error", "message": "Rating must be between 0 and 5"}, status=400)
        except ValueError:
            return JsonResponse({"status": "error", "message": "Invalid rating value"}, status=400)

        review.alat_olahraga = alat
        review.review_text = review_text
        review.rating = rating
        review.save()

        return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
def delete_review_flutter(request):
    data = json.loads(request.body)
    review = get_object_or_404(Review, pk=data["review_id"])
    if request.method == 'POST':
        review.delete()

    return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
@login_required
def create_rating_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        alat_olahraga_id = data['alat_olahraga']
        rating_value = data['rating']
        comment = data['comment']

        if not all([alat_olahraga_id, rating_value is not None, comment]):
            return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)

        try:
            alat = AlatOlahraga.objects.get(id=alat_olahraga_id)
        except AlatOlahraga.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Alat Olahraga does not exist"}, status=400)

        rating = Rating.objects.create(
            user=request.user,
            alat_olahraga=alat,
            rating=float(rating_value),
            comment=comment
        )

        rating.save()

        return JsonResponse({"status": "success", "rating_id": rating.pk}, status=201)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
@login_required
def edit_rating_flutter(request, pk):
    rating = get_object_or_404(Rating, pk=pk)

    if request.method == 'GET':
        alat_list = AlatOlahraga.objects.all()
        data = {
            "status": "success",
            "rating": {
                "id": rating.pk,
                "alat_olahraga": rating.alat_olahraga.pk,
                "comment": rating.comment,
                "rating": rating.rating,
            },
            "alat_olahraga_list": [
                {
                    "pk": alat.pk,
                    "alat_olahraga": alat.alat_olahraga,
                }
                for alat in alat_list
            ]
        }
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        
        data = json.loads(request.body)
        alat_olahraga_pk = data['alat_olahraga']
        comment = data['comment']
        rating_value = data['rating']

        if not all([alat_olahraga_pk, comment, rating_value is not None]):
            return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)

        try:
            alat = AlatOlahraga.objects.get(pk=alat_olahraga_pk)
        except AlatOlahraga.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Alat Olahraga does not exist"}, status=400)

        try:
            rating_float = float(rating_value)
            if rating_float < 0 or rating_float > 5:
                return JsonResponse({"status": "error", "message": "Rating must be between 0 and 5"}, status=400)
        except ValueError:
            return JsonResponse({"status": "error", "message": "Invalid rating value"}, status=400)

        rating.alat_olahraga = alat
        rating.comment = comment
        rating.rating = rating_float
        rating.save()

        return JsonResponse({"status": "success"}, status=200)


@csrf_exempt
@login_required
def delete_rating_flutter(request):
    if request.method == 'POST':
            data = json.loads(request.body)
            rating_id = data['rating_id']
            rating = get_object_or_404(Rating, pk=rating_id)
            rating.delete()
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    

@csrf_exempt
@login_required
def create_commentrating_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        article_id = data['article_id']
        name = data['name']
        rating = data['rating']
        comment = data['comment']

        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Article does not exist"}, status=400)

        comrat = CommentRatingArticle.objects.create(
            article=article,
            user=request.user,
            name=name,
            rating=rating,
            comment=comment
        )
        comrat.save()

        return JsonResponse({"status": "success", "id": comrat.pk}, status=201)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
@csrf_exempt
@require_http_methods(["GET", "POST"])
def edit_commentrating_flutter(request, pk):

    comrat = get_object_or_404(CommentRatingArticle, pk=pk)

    if request.method == 'GET':
        article_list = Article.objects.all()
        data = {
            "status": "success",
            "commentrating": {
                "id": comrat.pk,
                "article_id": comrat.article.pk,
                "name": comrat.name,
                "rating": comrat.rating,
                "comment": comrat.comment or "",
            },
            "article_list": [
                {
                    "pk": article.pk,
                    "title": article.title,
                }
                for article in article_list
            ]
        }
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        
        data = json.loads(request.body)
        article_id = data['article_id']
        name = data['name']
        rating = data['rating']
        comment = data['comment']

        try:
            rating = float(rating)
            if rating < 0 or rating > 5:
                return JsonResponse({"status": "error", "message": "Rating must be between 0 and 5"}, status=400)
        except ValueError:
            return JsonResponse({"status": "error", "message": "Invalid rating value"}, status=400)

        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Article does not exist"}, status=400)

        comrat.article = article
        comrat.name = name
        comrat.rating = rating
        comrat.comment = comment
        comrat.save()

        return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
def delete_commentrating_flutter(request):
    if request.method == 'POST':
    
        data = json.loads(request.body)
        comrat_id = data["id"]

        comrat = get_object_or_404(CommentRatingArticle, pk=comrat_id)
        comrat.delete()
        return JsonResponse({"status": "success"}, status=200)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

        



# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import Review, Rating

# @login_required
# def profile(request):
#     user_reviews = Review.objects.filter(user=request.user)
#     user_ratings = Rating.objects.filter(user=request.user)

#     context = {
#         'user': request.user,
#         'user_reviews': user_reviews,
#         'user_ratings': user_ratings,
#     }
#     return render(request, 'profile.html', context)
