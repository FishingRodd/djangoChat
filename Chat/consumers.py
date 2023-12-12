from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer,DenyConnection
from asgiref.sync import async_to_sync

from rest_framework_simplejwt.serializers import TokenVerifySerializer

# def verify_token(token):
#     serializer = TokenVerifySerializer(data={'token': token})
#     try:
#         serializer.is_valid(raise_exception=True)
#     except Exception as e:
#         # Token is invalid
#         return False
#     return True


class ChatConsumer(WebsocketConsumer):
    http_user = True         # 设置为 ``True`` 将会自动从 HTTP cookie 中登录用户，因此可以省去 channel_session_user 的设置。
    strict_ordering = False  # 默认设置
    # channel_session = True   # 设置为 ``True`` 将会自动将 channel layer session 与 Django session 关联起来，因此可以省去 channel_session_user 的设置。

    @classmethod
    def verifyToken(self,header):
        result = [t[-1].decode() for t in header if t[0].decode() == 'authorization']
        if result: # 列表非空
            token = result[0].split(' ')[-1]
            serializer = TokenVerifySerializer(data={'token': token})
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e:
                # Token is invalid
                # return False
                raise DenyConnection()
            return True
        else:
            raise DenyConnection()

    def connect(self):
        """连接开始
        """
        self.verifyToken(self.scope['headers'])

        # 将当前频道加入频道组
        self.room_group_name = 'chat_room'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # 接受所有websocket请求
        self.accept()

    def receive(self,text_data):
        """接收到信息时调用的函数
        """
        # self.send(text_data=text_data)
        # 发送消息到频道组，频道组调用chat_message方法
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data
            }
        )

    def disconnect(self, message, **kw):
        """断开连接时将会被调用
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        # raise StopConsumer()

    # 从频道组接收到消息后执行方法
    def chat_message(self, event):
        message = event['message']

        # 通过websocket发送消息到客户端
        self.send(text_data=message)