from django.forms import ModelForm
from main.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "review"]  # Menyertakan field rating dan review
