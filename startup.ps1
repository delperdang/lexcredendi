docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email steve.delperdang@gmail.com --agree-tos --no-eff-email -d lexcredendi.mooo.com
docker-compose up -d --build
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py makemigrations --no-input
docker-compose exec web python manage.py migrate --no-input