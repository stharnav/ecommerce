# from django.core.management.base import BaseCommand
# from backend.models import User
# from django.contrib.auth.hashers import make_password


# class Command(BaseCommand):
#     help = 'Seed the database with an admin user'

#     def handle(self, *args, **kwargs):
#         UserModel = User  # ✅ Use the model class, not an instance

#         # Create admin user if it doesn't exist
#         if not UserModel.objects.filter(first_name='Admin').exists():
#             UserModel.objects.create(
#                 first_name='Admin',
#                 last_name='User',
#                 username='admin',
#                 password=make_password('admin123'),
#                 sex=2,
#                 date_of_birth='1990-01-01',
#                 role=0,
#                 address='123 Admin St, Admin City'
#             )
#             self.stdout.write(self.style.SUCCESS(
#                 'Admin user created successfully!'))
#         else:
#             self.stdout.write(self.style.WARNING('Admin user already exists.'))


from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Seed the database with a default admin user'

    def handle(self, *args, **kwargs):
        username = 'admin'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS(
                'Admin user created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
