from django.urls import path
from authentication.views import login_api, logout_api, register_api

app_name = 'authentication'

urlpatterns = [
    path('login/', login_api, name='login'),
    path('register/', register_api, name='register'),
    path('logout/', logout_api, name='logout'),
]