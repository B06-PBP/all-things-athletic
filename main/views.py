# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review

def show_main(request):
    return render(request, 'main/main.html')

def list_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'main/review_list.html', {'reviews': reviews})

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:list_reviews')
    else:
        form = ReviewForm()
    return render(request, 'main/review_form.html', {'form': form})

def edit_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('main:list_reviews')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'main/review_form.html', {'form': form})

def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('main:list_reviews')
    return render(request, 'main/review_confirm_delete.html', {'review': review})
