import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Add these settings for production
DEBUG = False
ALLOWED_HOSTS = ['*.render.com', 'your-app-name.onrender.com']  # Replace with your actual domain

# Configure static file serving
MIDDLEWARE = [
    # ... other middleware ...
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'