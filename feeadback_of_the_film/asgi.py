import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from saport.routing import ws_urlpatterns



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feeadback_of_the_film.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(ws_urlpatterns)
        )
    }
)

