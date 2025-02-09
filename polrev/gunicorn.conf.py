import multiprocessing
import os

# Bind Gunicorn to all interfaces inside the container
bind = "0.0.0.0:8000"

# Worker settings (for a WSGI app)
workers = multiprocessing.cpu_count() * 2 + 1  # Recommended formula
worker_class = "sync"  # Default synchronous workers
timeout = 30  # Request timeout in seconds
graceful_timeout = 30  # Grace period before forcefully killing workers
keepalive = 5  # Keep connections open for 5 seconds

# Process management
preload_app = True  # Load the app before workers are forked (better memory usage)
max_requests = 1000  # Auto-restart workers after 1000 requests (prevents memory leaks)
max_requests_jitter = 50  # Spread out worker restarts

# Security & Reverse Proxy settings
forwarded_allow_ips = "*"  # Trust all incoming proxies (handled by Traefik)
proxy_allow_ips = "*"  # Trust all incoming proxies
limit_request_line = 4096  # Prevent excessively long requests
limit_request_fields = 100  # Prevent too many headers
limit_request_field_size = 8190  # Prevent large headers

# Logging (log to stdout for Docker)
loglevel = "info"
accesslog = "-"  # Log access requests to stdout
errorlog = "-"  # Log errors to stderr

# Daemon mode should be off in Docker
daemon = False
