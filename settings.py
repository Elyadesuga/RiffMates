import os

# Базовые настройки для разработки и production
ALLOWED_HOSTS = [
    'riffmates-v4ph.onrender.com',  # Ваш конкретный хост
    '.onrender.com',                # Все поддомены Render
    'localhost',
    '127.0.0.1',
    '[::1]'                         # IPv6 localhost
]

# Дополнительная защита для production
if os.environ.get('DEBUG', 'False') == 'False':
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
