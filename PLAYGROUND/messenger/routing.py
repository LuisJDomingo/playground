from django.urls import re_path
from . import consumers


print("[ROUTING] Cargando routing.py de messenger")

# WebSocket URL routing for the messenger app
websocket_urlpatterns = [
    re_path(r'ws/messenger/(?P<thread_id>\d+)/$', consumers.ThreadConsumer.as_asgi()),
]

print(f"[ROUTING] Patrones WebSocket registrados: {websocket_urlpatterns}")