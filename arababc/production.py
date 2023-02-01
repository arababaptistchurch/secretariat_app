from .settings import *
import os
import mimetypes


mimetypes.add_type("text/css", ".css", True)

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']
                        ] if 'WEBSITE_HOSTNAME' in os.environ else []


# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# DBHOST is only the server name, not the full URL
# hostname = os.environ['DBHOST']

# Configure Postgres database; the full username for PostgreSQL flexible server is
# username (not @sever-name).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'araba.postgres.database.azure.com',
        'USER': 'araba',
        'PASSWORD': '##Icui4cu4u'
    }
}
