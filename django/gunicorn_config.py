bind = "0.0.0.0:8000"
module = "lexcredendi.wsgi:application"

workers = 2
worker_connections = 1000
threads = 4

# TODO: uncomment these lines once SSL is active
certfile = "/etc/letsencrypt/live/lexcredendi.app/fullchain.pem"
keyfile = "/etc/letsencrypt/live/lexcredendi.app/privkey.pem"