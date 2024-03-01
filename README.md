# LexCredendi

This is a simple Django project configured to be deployed in Docker containers with a PostgreSQL backend and Nginx web server. The function of this web app is to provide quick access to prayers, apologetics, daily readings and more to support Catholic users.

## Features

- Django web framework
- PostgreSQL database support with psycopg
- Web Scraping with Beautiful Soup for calendar and readings
- Automatic timezone detection thanks to django-tz-detect
- Context processing of liturgical season colors using python-dateutil
- Dynamic Bible and Catechism link insertion for supported apps
- Feed of project updates using GitHub API

## Setup

Below are the basic commands I would use to setup and test locally.

### Setup part 1 - Clone the repo

```
mkdir ~/code/lexcredendi
cd ~/code/lexcredendi
git clone "https://github.com/delperdang/lexcredendi.git"
```

### Setup part 2 - Create virtual environment (linux/mac)

The .gitignore that comes with the project will ignore this virtual environment.

```
python -m venv venv
cd ~/code/lexcredendi/web
source ~/code/lexcredendi/venv/bin/activate
python -m pip install -r requirements.txt
```

### Setup part 2 - Create virtual environment (windows)

The .gitignore that comes with the project will ignore this virtual environment.

```
python -m venv venv
cd ~/code/lexcredendi
./code/lexcredendi/venv/Scripts/activate
cd ~/code/lexcredendi/web
python -m pip install -r requirements.txt
```

### Setup Part 3 - Create Environment variables

These evironment variables are necessary to run the web app, create a superuser, and connect to the database.

```
DEBUG=false
SECRET_KEY=foo
SUPERUSER_EMAL=bar
SUPERUSER_NAME=spam
SUPERUSER_PASS=eggs
POSTGRES_USER=trad
POSTGRES_PASSWORD=cath
ALLOWED_HOSTS=127.0.0.1 localhost
```

Before deploying to docker, these environment variables must be added to a .env file in the root directory of the project.

```
django_project
├── nginx
├── web
├── .env
├── .gitignore
├── docker-compose.yml
├── README.md
```

These settings are explicitly altered based on the `DEBUG` environment variable.

- settings.py - `DEBUG`
- settings.py - `DATABASES`
- urls.py - `urlpatterns`

## Deployment

It is possible to deploy to Docker immediately or to your own linux/windows server with a few minor adjustments.

### Docker

Before attempting to deploy to docker you should have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

#### Startup Procedure

```
docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email steve.delperdang@gmail.com --agree-tos --no-eff-email -d lexcredendi.mooo.com
```

```
docker-compose up -d --build
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py makemigrations --no-input
docker-compose exec web python manage.py migrate --no-input
```

#### Shutdown Procedure

**Warning**: this assumes you want to completely remove all volumes and images for a fresh start

```
docker-compose down --volumes
docker system prune -a --force
```

## Configuration

Once the project is deployed in docker or a custom server it needs to be configured and populated.

1. Open the site and visit `/createsuperuser` to generate a superuser. This will only perform an action if the superuser doesn't exist.
2. Open the site and visit `/admin` and login with the superuser credentials.
3. Begin uploading records using the import function for each applicable app (art has to be loaded one by one).
4. For pre-prepared csv uploads and religious art visit this [Google Drive](https://drive.google.com/drive/folders/1TffGjIoL3h4bUeAUnZdR_Pn1_Ob9BoOa) and request access.

## License

MIT License

Copyright (c) 2019 Steven Delperdang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
