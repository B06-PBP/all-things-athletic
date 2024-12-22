import json
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.forms import CustomUserCreationForm, CustomUserLoginForm

@csrf_exempt
def register_api(request):
    if request.method == 'POST':
        try:
            data = request.POST
        except json.JSONDecodeError:
            return JsonResponse({
                "status": False,
                "message": "Invalid JSON data."
            }, status=400)
        
        form = CustomUserCreationForm(data)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role', 'user')
            user.save()
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Registrasi berhasil, silakan login"
            }, status=201)
        else:
            errors = form.errors.get_json_data()
            return JsonResponse({
                "status": False,
                "message": "Registrasi gagal.",
                "errors": errors
            }, status=400)
    else:
        return JsonResponse({
            "status": False,
            "message": "Metode permintaan tidak valid. Hanya POST yang diizinkan."
        }, status=405)

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except json.JSONDecodeError:
            return JsonResponse({
                "status": False,
                "message": "Invalid JSON data."
            }, status=400)
        
        form = CustomUserLoginForm(data={'username': username, 'password': password})
        
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "userId": user.pk,
                "role": user.role,
                "status": True,
                "message": "Login berhasil!"
            }, status=200)
        else:
            # Kumpulkan semua error dari form
            errors = form.errors.get_json_data()
            return JsonResponse({
                "status": False,
                "message": "Login gagal.",
                "errors": errors
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Metode permintaan tidak valid. Hanya POST yang diizinkan."
        }, status=405)

@csrf_exempt
def logout_api(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            auth_logout(request)
            return JsonResponse({
                "username": username,
                "status": True,
                "message": "Logout berhasil!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "User tidak terautentikasi."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Metode permintaan tidak valid. Hanya POST yang diizinkan."
        }, status=405)
