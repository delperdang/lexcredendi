bind = "0.0.0.0:8000"
module = "lexcredendi.wsgi:application"

workers = 2
worker_connections = 1000
threads = 4

# TODO: comment these lines when encryption is not yet active
# certfile = "/etc/letsencrypt/live/lexcredendi.mooo.com/fullchain.pem"
# keyfile = "/etc/letsencrypt/live/lexcredendi.mooo.com/privkey.pem"