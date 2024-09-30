import os

bind = "0.0.0.0:8000"
module = "lexcredendi.wsgi:application"

workers = 2
worker_connections = 1000
threads = 4

if os.path.isfile("/etc/letsencrypt/live/lexcredendi.app/fullchain.pem"):
    certfile = "/etc/letsencrypt/live/lexcredendi.app/fullchain.pem"

if os.path.isfile("/etc/letsencrypt/live/lexcredendi.app/privkey.pem"):
    keyfile = "/etc/letsencrypt/live/lexcredendi.app/privkey.pem"
