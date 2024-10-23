from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Untuk input banyak kalimat
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),  # Input rating 1-5
        }
