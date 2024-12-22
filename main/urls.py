from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from main.views import (
    create_product_flutter, register, login_user, logout_user, show_main, show_articles, 
    get_article_details, show_article1, show_article2, show_article3, 
    show_article4, show_article5, show_article6, show_product, show_yoga, 
    show_cycling, show_tennis, show_boxing, show_badminton, show_basketball, 
    show_running, show_football, show_swimming, show_golf, create_alat, alat_list, delete_alat, edit_alat,
    rate_product, review_product, user_reviews_and_ratings, rating_list, rating_create,
    rating_list, rating_create, rating_edit, review_list, review_create, review_edit, rating_delete, review_delete, 
    show_alat_olahraga_json, show_rating_list_json, show_review_list_json, create_review_flutter, edit_review_flutter,
    delete_review_flutter, create_rating_flutter, edit_rating_flutter, delete_rating_flutter, get_username, get_alat,
    show_article_json, create_commentrating_flutter, edit_commentrating_flutter, delete_commentrating_flutter,
    show_article_commrat, user_reviews_flutter, user_ratings_flutter, seed_dataset
)
from main.views import register, login_user, logout_user
from main.views import show_main, show_articles, get_article_details
from main.views import show_article1, show_article2, show_article3, show_article4, show_article5, show_article6, seed_article
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
    path('create_alat/', create_alat, name='create_alat'),
    path('alat/<int:id>/edit/', edit_alat, name='edit_alat'), 
    path('alat_list/', alat_list, name='alat_list'),
    path('alat/<int:id>/delete/', delete_alat, name='delete_alat'),
    path('articles/<int:article_id>/', get_article_details, name='get_article_details'),
    path('articles/create-flutter/', create_commentrating_flutter, name='comrat_create'),
    path('articles/<int:pk>/edit-flutter/', edit_commentrating_flutter, name='comrat_edit'),
    path('articles/delete-flutter/', delete_commentrating_flutter, name='comrat_delete'),
    path('ratings/', rating_list, name='rating_list'),
    path('ratings/create/', rating_create, name='rating_create'),
    path('ratings/create-flutter/', create_rating_flutter, name='rating_create'),
    path('ratings/<int:pk>/edit/', rating_edit, name='rating_edit'),
    path('ratings/<int:pk>/edit-flutter/', edit_rating_flutter, name='rating_edit'),
    path('ratings/<int:pk>/delete/', rating_delete, name='rating_delete'),
    path('ratings/delete-flutter/', delete_rating_flutter, name='rating_delete'),
    path('show_alat_olahraga_json/', show_alat_olahraga_json, name='show_alat_olahraga_json'),
    path('show_article_json/', show_article_json, name='show_article_json'),
    path('show_rating_list_json/', show_rating_list_json, name='show_rating_list_json'),
    path('show_review_list_json/', show_review_list_json, name='show_review_list_json'),
    path('show_article_comrat_json/<int:pk>/', show_article_commrat, name='show_review_list_json'),
    path('username/<int:id>/', get_username, name='get_username'),
    path('alat/<int:id>/', get_alat, name='get_alat'),
    # Review URLs
    path('reviews/', review_list, name='review_list'),
    path('reviews/create/', review_create, name='review_create'),
    path('reviews/create-flutter/', create_review_flutter, name='review_create_flutter'),
    path('reviews/<int:pk>/edit/', review_edit, name='review_edit'),
    path('reviews/<int:pk>/edit-flutter/', edit_review_flutter, name='review_edit_flutter'),
    path('reviews/<int:pk>/delete/', review_delete, name='review_delete'),
    path('reviews/delete-flutter/', delete_review_flutter, name='review_delete'),
    path('rate/<int:alat_id>/', rate_product, name='rate_product'),
    path('review/<int:alat_id>/', review_product, name='review_product'),
    path('my-reviews-and-ratings/', user_reviews_and_ratings, name='user_reviews_and_ratings'),
    path('my-reviews/<int:id>/', user_reviews_flutter, name='user_reviews'),
    path('my-ratings/<int:id>/', user_ratings_flutter, name='user_ratings'),
    path('admin/', admin.site.urls),
    path('articles/<int:article_id>/', get_article_details, name='get_article_details'),
    path('seed-article/', seed_article, name='seed_article'),
    path('seed-dataset/', seed_dataset, name='seed_dataset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)