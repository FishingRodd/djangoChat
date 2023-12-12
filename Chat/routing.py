'''
当 Django 接受 HTTP 请求时, 它会根据根 URLconf 以查找视图函数, 然后调用视图函数来处理请求。
同样, 当 channels 接受 WebSocket 连接时, 它也会根据根路由配置去查找相应的处理方法。
只不过channels的路由不在urls.py中配置，处理方法也不写在views.py。
在channels中，这两个文件分别变成了routing.py和consumers.py。
这样的好处是不用和django的常规应用混在一起。
'''
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'chat/room', consumers.ChatConsumer.as_asgi()),
]