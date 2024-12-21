from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    role = models.CharField(max_length=5, choices=USER_ROLE_CHOICES, default='user')
    first_name = models.CharField(max_length=30)  # First name
    last_name = models.CharField(max_length=30)   # Last name
    email = models.EmailField(unique=True)         # Email (should be unique)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile picture

    # Set related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Article(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    full_description = models.TextField()

    def __str__(self):
        return self.title

class AlatOlahraga(models.Model):
    cabang_olahraga = models.CharField(max_length=100)  # Untuk "Cabang Olahraga"
    alat_olahraga = models.CharField(max_length=100)  # Untuk "Alat Olahraga"
    deskripsi = models.TextField()  # Untuk "Description"
    harga = models.CharField(max_length=20)  # Untuk "Rata-rata harga"
    toko = models.CharField(max_length=200)  # Untuk "Toko yang menjual"
    rating = models.FloatField()  # Untuk "Rata-rata Rating"
    gambar = models.URLField(max_length=200)  # Untuk "Referensi Gambar"

    def __str__(self):
        return self.alat_olahraga

class Rating(models.Model):
    alat_olahraga = models.ForeignKey(
        'AlatOlahraga', 
        related_name='alat_ratings', 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='user_ratings', 
        on_delete=models.CASCADE
    )
    rating = models.FloatField()  # Rating value, e.g., between 0 and 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('alat_olahraga', 'user')  # Prevent duplicate ratings per user per product

    def __str__(self):
        return f"{self.user} - {self.rating} for {self.alat_olahraga}"


class Review(models.Model):
    alat_olahraga = models.ForeignKey(
        'AlatOlahraga', 
        related_name='alat_reviews', 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='user_reviews', 
        on_delete=models.CASCADE
    )
    review_text = models.TextField()
    rating = models.FloatField()  # Optionally include rating in review, between 0 and 5
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user} for {self.alat_olahraga}"
    
class CommentRatingArticle(models.Model):
    article = models.ForeignKey(
        'Article', 
        related_name='article', 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='user_article_comrat', 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    rating = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.rating} for {self.article}"