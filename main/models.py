from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField()  # Rating dari 1 hingga 5
    comment = models.TextField()  # Menyimpan banyak kalimat
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.name} - Rating: {self.rating}'
