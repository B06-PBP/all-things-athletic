<<<<<<< HEAD
import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # menggunakan UUID sebagai primary key
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),  # Nilai minimum
            MaxValueValidator(5)   # Nilai maksimum
        ]
    )  # Rating dari 0 hingga 5
    review = models.TextField()  # Menyimpan banyak kalimat
    date = models.DateTimeField(auto_now_add=True)  # Tanggal pembuatan review

    def __str__(self):
        return f'Rating: {self.rating}'
=======
from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
>>>>>>> origin/shafa
