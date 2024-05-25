# LexCredendi

This is a simple Django project configured to be deployed in Docker containers with a PostgreSQL backend and Nginx web server. The function of this web app is to provide quick access to Catholic prayers, apologetics, daily readings, sacred art and much more.

## Features

- Django web framework
- PostgreSQL database support with psycopg
- Web Scraping with Beautiful Soup for calendar and readings
- Context processing of liturgical season colors using python-dateutil
- Dynamic Bible and Catechism link insertion for supported apps
- A live feed of project updates using GitHub API
- Dynamic DNS from oznu/cloudflare-ddns
- SSL Certificate management from certbot/certbot 

## Setup

Below are the basic steps use to setup and test the web app with docker.

### Setup part 1 - Install Dev Container

1) Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2) Install [VS Code](https://code.visualstudio.com/)
3) Install the Extension "Dev Containers"

### Setup part 2 - Clone the Repository

1) Download the [master branch](https://github.com/delperdang/lexcredendi/archive/refs/heads/master.zip) as a zip file
2) Unzip and copy the contents to a directory of your choosing (e.g. `~/code/lexcredendi`)

### Setup Part 3 - Prepare the Workspace

1) Close any current workspace (File > Close Workspace)
2) Close any remote connection (File > Close Remote Connection)
3) Open the project workspace file (File > Open Workspace from File). The file is called `lexcredendi.code-workspace` and is located in the root directory of the project.
4) Open the command palette (View > Command Palette) and enter `>Dev Containers: Rebuild and Reopen in Container`

### Setup Part 4 - Setup and Run Django

Run the following commands to setup and run Django with the test web server
```
cd django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
You will now be able to access your test server from a browser on your host machine at `localhost:8000`

## Deployment

### Docker

Before attempting to deploy to docker you should have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

### Environment variables

These evironment variables are necessary to run the web app, create a superuser, connect to the database, and update DNS.

```
DEBUG=false
SECRET_KEY=foo
SUPERUSER_EMAL=bar
SUPERUSER_NAME=spam
SUPERUSER_PASS=eggs
POSTGRES_USER=trad
POSTGRES_PASSWORD=cath
ALLOWED_HOSTS=lexcredendi.app www.lexcredendi.app
API_KEY=cloudflare
ZONE=lexcredendi.app
PROXIED=false
```

Before deploying in docker, these environment variables must be added to a `prod.env` file in the root directory of the project.

```
lexcredendi
├── .devcontainer
├── .github
├── certbot
├── django
├── nginx
├── scripts
├── .gitignore
├── docker-compose.yml
├── lexcredendi.code-workspace
├── prod.env
├── README.md
```

#### Retrieving an SSL Cert

1) Follow the comments in `certbot/Dockerfile`
2) Follow the comments in `django/gunicorn_config.py`
3) Follow the comments in `nginx/Dockerfile`
4) Run `scripts/certonly.ps1` (if not on Windows try the command from the script in you default shell)
5) Assuming success... open Docker Desktop, go to Volumes, select lexcredendi_certbot-conf, and save the following files:
    - `/live/lexcredendi.app/fullchain.pem`
    - `/live/lexcredendi.app/fullchain.pem`
6) Copy those saved files to the `certbot` directory in the project
7) Repeat steps 1-3 following the comments for once SSL is active
8) Run `scripts/shutdown.ps1` (if not on Windows try the command from the script in you default shell)
9) Run `scripts/startup.ps1` (if not on Windows try the command from the script in you default shell)

#### Startup Procedure

Run `scripts/startup.ps1` to build and start up all the docker containers

#### Shutdown Procedures

Run `scripts/shutdown.ps1` to destroy all containers, volumes, and images

## Configuration

Once the project is deployed it needs to be configured and populated.

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
