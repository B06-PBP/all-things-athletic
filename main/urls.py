from django.urls import path
from .views import show_main, create_review, edit_review, delete_review, list_reviews

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('reviews/', list_reviews, name='list_reviews'),
    path('reviews/create/', create_review, name='create_review'),
    path('reviews/edit/<int:id>/', edit_review, name='edit_review'),
    path('reviews/delete/<int:id>/', delete_review, name='delete_review'),
]
