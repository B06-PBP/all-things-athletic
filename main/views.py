from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import JsonResponse

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# def logout_user(request):
#     logout(request)
#     return redirect('main:login')

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