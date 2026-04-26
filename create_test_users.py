import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secure_api.settings')
django.setup()

from django.contrib.auth.models import User, Group

test_users_data = [
    {"username": "admin1", "password": "password123", "group": "Admin"},
    {"username": "faculty1", "password": "password123", "group": "Faculty"},
    {"username": "student1", "password": "password123", "group": "Student"},
]

for user_data in test_users_data:
    user, created = User.objects.get_or_create(username=user_data["username"])
    if created:
        user.set_password(user_data["password"])
        user.save()
        group = Group.objects.get(name=user_data["group"])
        user.groups.add(group)
        print(f"Created {user_data['username']} and added to {user_data['group']} group.")
    else:
        print(f"User {user_data['username']} already exists.")
