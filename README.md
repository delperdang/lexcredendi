# LexCredendi

This is a simple Django 3 project configured to be deployed to Docker with a PostgreSQL backend. The function of this web app is to provide quick access to prayers, apologetics, readings and more to support Catholic users.

## Features

- Django web framework
- PostgreSQL database support with psycopg
- Web Scraping with Beautiful Soup for calendar and readings
- Automatic timezone detection thanks to django-tz-detect
- Context processing of liturgical season using python-dateutil
- Automatic protocol elevation (HTTP to HTTPS)
- Feed of project updates via requests + GitHub api

## How to install

```bash
$ git clone https://github.com/delperdang/lexcredendi
$ pip install -r requirements.txt
```

## Environment variables

These evironment variables are necessary to run the web app and automatically configure a superuser.

```
SECRET_KEY='foo'
SUPERUSER_PASS='bar'
SUPERUSER_NAME='spam'
SUPERUSER_EMAL='eggs'
```

These environment variables are necessary to deploy successfully with a PostgreSQL backend.

```
POSTGRES_USER='spam'
POSTGRES_PASSWORD='eggs'
```

These settings are explicitly altered based on the host environment and by proxy the `DEBUG` value.

```
settings.py DEBUG
settings.py DATABASES
urls.py urlpatterns
offcanvas.js location.protocol
```

## Deployment

It is possible to deploy to Docker or to your own linux server with a few adjustments.

### Docker

```bash
$ docker-compose build
$ docker-compose up -d
```

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
