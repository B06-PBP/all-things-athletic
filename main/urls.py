from django.urls import path
from main.views import register, login_user, logout_user
from main.views import show_main, show_articles, get_article_details
from main.views import show_article1, show_article2, show_article3, show_article4, show_article5, show_article6
from main.views import show_product, show_yoga, show_cycling, show_tennis, show_boxing, show_badminton, show_basketball, show_running, show_football, show_swimming, show_golf

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('articles/', show_articles, name='show_articles'),
    path('articles1/', show_article1, name='show_article1'),
    path('articles2/', show_article2, name='show_article2'),
    path('articles3/', show_article3, name='show_article3'),
    path('articles4/', show_article4, name='show_article4'),
    path('articles5/', show_article5, name='show_article5'),
    path('articles6/', show_article6, name='show_article6'),
    path('products/', show_product, name='show_product'),
    path('yoga/', show_yoga, name='show_yoga'),
    path('cycling/', show_cycling, name='show_cycling'),
    path('tennis/', show_tennis, name='show_tennis'),
    path('boxing/', show_boxing, name='show_boxing'),
    path('badminton/', show_badminton, name='show_badminton'),
    path('basketball/', show_basketball, name='show_basketball'),
    path('running/', show_running, name='show_running'),
    path('football/', show_football, name='show_football'),
    path('swimming/', show_swimming, name='show_swimming'),
    path('golf/', show_golf, name='show_golf'),
    path('articles/<int:article_id>/', get_article_details, name='get_article_details'),
]