from django.urls import path
from main.views import show_product

app_name = 'main'

urlpatterns = [
    path('', show_product, name='home'),
    path('product/', show_product, name='show_product'),
]