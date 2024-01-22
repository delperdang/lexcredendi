docker-compose build
docker-compose up -d
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py makemigrations --no-input
docker-compose exec web python manage.py migrate --no-input