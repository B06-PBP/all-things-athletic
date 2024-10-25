from django.db import models

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