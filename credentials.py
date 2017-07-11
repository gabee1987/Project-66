import os
import psycopg2
import urllib

# Database connection string
# DATABASE_URL=postgres://user:password@host:port/database
urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
connection_data = {
    'dbname': url.path[1:],
    'user': url.username,
    'host': url.hostname,
    'password': url.password,
    'port': url.port
}

# Secret key for sessions
secret_key = os.environ.get('SECRET_KEY')
