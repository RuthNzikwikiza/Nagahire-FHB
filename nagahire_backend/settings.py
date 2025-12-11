from pathlib import Path
import os
import dj_database_url
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# BASIC SETTINGS
# -------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-d-ik@*neu=o5g-q+wpelw^qbc6+)zm^201y1f9@if93q82k3i1')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'nagahire-fhb.onrender.com',
    'localhost',
    '127.0.0.1',
]

# -------------------------
# INSTALLED APPS
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'cloudinary',
    'cloudinary_storage',
    'corsheaders',
    'rest_framework',

    # Your app
    'shop',
]

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------
# CORS
# -------------------------
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.onrender.com",
    "http://localhost:3000",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

# -------------------------
# TEMPLATES
# -------------------------
ROOT_URLCONF = 'nagahire_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nagahire_backend.wsgi.application'

# -------------------------
# DATABASE
# -------------------------
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ['DATABASE_URL'],
            conn_max_age=600,
            conn_health_checks=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# -------------------------
# PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Kigali'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC FILES
# -------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------
# MEDIA (LOCAL)
# -------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# -------------------------
# CLOUDINARY (PRODUCTION MEDIA)
# -------------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'dmewkrxzk'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '821886382863267'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', ''),
}

cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE["CLOUD_NAME"],
    api_key=CLOUDINARY_STORAGE["API_KEY"],
    api_secret=CLOUDINARY_STORAGE["API_SECRET"],
)

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# -------------------------
# SECURITY (ONLY PRODUCTION)
# -------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'DENY'

# -------------------------
# LOGGING
# -------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
