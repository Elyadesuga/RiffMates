import os
ALLOWED_HOSTS = ['*']

# Дополнительная защита для production
if os.environ.get('DEBUG', 'False') == 'False':
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
