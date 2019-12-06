import os
from django.contrib.auth.models import User

if not User.objects.filter(username='dieselpwr').exists():
    User.objects.create_superuser('dieselpwr', 'dieselpwr99@gmail.com', os.environ['SUPERUSER_PASS'])
