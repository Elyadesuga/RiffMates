
import os
RENDER_EXTERNAL_HOSTNAME = os.environ.get('riffmates-v4ph.onrender.com')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(riffmates-v4ph.onrender.com)
