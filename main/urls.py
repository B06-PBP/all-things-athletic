from django.urls import path
from main.views import show_main, show_articles #get_article_details
from main.views import show_article1, show_article2, show_article3, show_article4, show_article5, show_article6

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('articles/', show_articles, name='show_articles'),
    path('articles1/', show_article1, name='show_article1'),
    path('articles2/', show_article2, name='show_article2'),
    path('articles3/', show_article3, name='show_article3'),
    path('articles4/', show_article4, name='show_article4'),
    path('articles5/', show_article5, name='show_article5'),
    path('articles6/', show_article6, name='show_article6'),
    #path('articles/<int:article_id>/', get_article_details, name='get_article_details'),
]