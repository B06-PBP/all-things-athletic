from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306214025',
        'name': 'Shafa Amira Azka',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)