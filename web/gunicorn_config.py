bind = "0.0.0.0:8000"
module = "lexcredendi.wsgi:application"

workers = 2
worker_connections = 1000
threads = 4

# TODO: uncomment these lines when encryption is active
# certfile = "/etc/letsencrypt/live/lexcredendi.ignorelist.com/fullchain.pem"
# keyfile = "/etc/letsencrypt/live/lexcredendi.ignorelist.com/privkey.pem"