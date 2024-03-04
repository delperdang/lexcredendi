# Add --dry-run to the below to test without writing new cert files
# Update nginx to http conf and comment SSL lines from gunicorn config before running
docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email steve.delperdang@gmail.com --agree-tos --no-eff-email -d lexcredendi.app