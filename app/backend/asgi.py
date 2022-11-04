import os
from channels.asgi import get_channel_layer

# from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
channel_layer = get_channel_layer()
