docker-compose up -d --build
docker-compose exec django python manage.py collectstatic --no-input
docker-compose exec django python manage.py makemigrations --no-input
docker-compose exec django python manage.py migrate --no-input