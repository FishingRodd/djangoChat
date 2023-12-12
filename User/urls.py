from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AuthViewSet, UserViewSet

router = SimpleRouter()

urlpatterns = [
    path('login', AuthViewSet.as_view({'post': 'Login'}), name='Login'),
    path('register', AuthViewSet.as_view({'post': 'Register'}), name='Register'),

    path('getAll', UserViewSet.as_view({'get': 'GetUserAll'}), name='GetUserAll'),
]