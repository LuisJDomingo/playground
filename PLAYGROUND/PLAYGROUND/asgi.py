import os
import django
from django.core.asgi import get_asgi_application

print("=" * 60)
print("[ASGI] ¡EJECUTANDO ASGI.PY!")
print("=" * 60)

# Configurar Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PLAYGROUND.settings')
django.setup()

print("[ASGI] Django configurado")

# Importar lo que necesitamos de channels
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path

print("[ASGI] Importando consumer...")

from messenger.consumers import ThreadConsumer

print("[ASGI] Consumer importado exitosamente")

# Definir las rutas WebSocket
from  messenger.routing import websocket_urlpatterns


print(f"[ASGI] Rutas WebSocket definidas: {websocket_urlpatterns}")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

print("[ASGI] ¡CONFIGURACIÓN ASGI COMPLETADA!")
print("=" * 60)