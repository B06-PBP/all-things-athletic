from django.urls import path
from main.views import show_product

app_name = 'main'

urlpatterns = [
    path('products/', show_product, name='show_product'),
]