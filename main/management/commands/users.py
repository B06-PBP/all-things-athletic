from django.core.management.base import BaseCommand
from main.models import CustomUser  # Adjust import based on your model's location

class Command(BaseCommand):
    help = 'Seed database with admin and user roles'

    def handle(self, *args, **options):
        # Create admin user
        admin_user = CustomUser.objects.create_user(
            username='admin_user',
            password='admin_password',
            first_name='Admin',
            last_name='User',
            email='admin@example.com',
            role='admin'  # Set role to admin
        )
        self.stdout.write(self.style.SUCCESS(f'Admin user created: {admin_user.username}'))

        # Create regular user
        regular_user = CustomUser.objects.create_user(
            username='regular_user',
            password='user_password',
            first_name='Regular',
            last_name='User',
            email='user@example.com',
            role='user'  # Set role to user
        )
        self.stdout.write(self.style.SUCCESS(f'Regular user created: {regular_user.username}'))
