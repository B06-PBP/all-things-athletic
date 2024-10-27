from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Article, AlatOlahraga, Rating, Review

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'profile_picture')}),
    )

# Register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)
admin.site.register(AlatOlahraga)
admin.site.register(Rating)
admin.site.register(Review)
