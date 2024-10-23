from django.urls import path
from main.views import show_main, edit_review, delete_review

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('edit/<int:pk>/', edit_review, name='edit_review'),
    path('delete/<int:pk>/', delete_review, name='delete_review'),
]
