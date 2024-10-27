from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, AlatOlahraga, Rating, Review
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def confirm_login_allowed(self, user):
        # Optionally, you can add custom validation here if you have additional conditions for logging in.
        if not user.is_active:
            raise forms.ValidationError("This account is inactive.", code='inactive')
        if not user.is_authenticated:
            raise forms.ValidationError("Authentication failed.", code='not_authenticated')
        
class AlatOlahragaForm(forms.ModelForm):
    class Meta:
        model = AlatOlahraga  # Ensure this matches your model
        fields = '__all__'  # Adjust to specify fields if needed
        rating = forms.DecimalField(
        max_digits=3,  # Adjust as necessary
        decimal_places=1,  # Allow one decimal place
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={
            'step': '0.1',  # Allow decimal input
        })
    )

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['alat_olahraga', 'rating', 'comment']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['alat_olahraga', 'rating', 'review_text']