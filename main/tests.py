from django.test import TestCase, Client
from django.utils import timezone
from .models import Review

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_review_creation(self):
        # Membuat review baru
        review = Review.objects.create(
            rating=4,
            review="Ini adalah review yang baik.",
        )
        self.assertEqual(review.rating, 4)  # Memastikan rating sesuai
        self.assertEqual(review.review, "Ini adalah review yang baik.")  # Memastikan review sesuai

    def test_rating_bounds(self):
        # Menguji batasan rating
        with self.assertRaises(ValueError):
            Review.objects.create(rating=6, review="Rating terlalu tinggi.")  # Harus menghasilkan ValueError

        with self.assertRaises(ValueError):
            Review.objects.create(rating=-1, review="Rating terlalu rendah.")  # Harus menghasilkan ValueError