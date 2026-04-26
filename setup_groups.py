import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import Group

groups = ['Admin', 'Faculty', 'Student']
for g in groups:
    group, created = Group.objects.get_or_create(name=g)
    if created:
        print(f"Group '{g}' created.")
    else:
        print(f"Group '{g}' already exists.")
