import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='dieselpwr').exists():
            User.objects.create_superuser('dieselpwr',
                                          'dieselpwr99@gmail.com',
                                          os.environ['SUPERUSER_PASS'])
