from .models import User
from .serializers import UserSerializer

from django.utils import timezone

from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class AuthViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def Register(self, request):
        nickname = request.data.get('nickname')
        password = request.data.get('password')
        try:
            user = User.objects.create(nickname=nickname, password=password)
        except Exception as e:
            if 'UNIQUE constraint failed: User_user.nickname' == str(e):
                raise exceptions.AuthenticationFailed({
                    'code': '-1',
                    'msg': '用户名已存在'
                })
            else:
                raise exceptions.AuthenticationFailed({
                    'code': '-1',
                    'msg': '注册失败'
                })
        return Response({
            'code': '0',
            'msg': '注册成功',
            'result': {
                'uid': user.uid,
                'nickname': user.nickname,
            }
        })

    def Login(self, request):
        nickname = request.data.get('nickname')
        password = request.data.get('password')
        try:
            user = User.objects.get(nickname=nickname)
            print('user.password==password:',user.password==password)
            if user.password==password: # 密码检查
                pass
            else:
                raise exceptions.AuthenticationFailed()
        except Exception as e:
            if isinstance(e, exceptions.AuthenticationFailed):
                raise exceptions.AuthenticationFailed({
                    'code': '-1',
                    'msg': '密码错误'
                })
            elif 'User matching query does not exist.' == str(e):
                raise exceptions.AuthenticationFailed({
                    'code': '-1',
                    'msg': '账号错误'
                })
            user = None

        if user:
            user.last_login = timezone.now() # 登陆时间更新
            refresh = RefreshToken.for_user(user)

            user.save()
            return Response({
                'code': '0',
                'msg': '登录成功',
                'result':{
                    # 'refresh': str(refresh),
                    'token': str(refresh.access_token),
                    'userinfo':{
                        'uid': user.uid,
                        'nickname': user.nickname,
                    }
                }
            })

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer

    def GetUserAll(self, request):
        try:
            uid = request.data['uid'] # 获取关键字

            user = User.objects.get(uid=uid) # 获得模型类
            s = self.get_serializer(instance=user) # 反序列化验证，返回json格式
            return Response({
                'code': '0',
                'msg': 'success',
                'result': s.data
            })
        except Exception as e:
            if 'uid' in str(e):
                # if (bool(request.data) == False) or (not request.data['uid']):
                raise exceptions.AuthenticationFailed({
                    'code': '-1',
                    'msg': 'uid不能为空'
                })
            else:
                print(e)
                raise exceptions.AuthenticationFailed({
                    'code': '-1',
                    'msg': '获取失败'
                })