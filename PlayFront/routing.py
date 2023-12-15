from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"play.socket/", consumers.playSocket.as_asgi()),
]