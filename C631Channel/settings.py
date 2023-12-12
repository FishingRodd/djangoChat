import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@-++2yct-xa64t0=5uqu7m^h7qwdj^^kr0t-st=^zz!))d-n4o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'User.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'daphne', # https://blog.csdn.net/qq_25218219/article/details/131752459
    'django.contrib.staticfiles',
    'channels',
    'User', #app1
    'Chat', #app2
]
ASGI_APPLICATION = 'C631Channel.asgi.application'
# django runserver时默认使用WSGI规范，而他不支持websocket和异步等操作，所以在这里修改调整，我们需要使用ASGI规范
CHANNEL_LAYERS = {
     "default": {
         "BACKEND": "channels.layers.InMemoryChannelLayer"
     }
 }
# 生产环境中使用redis做后台，安装channels_redis
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#             # 或"hosts": [os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1')],
#         },
#     },
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,  # 允许用户获取新的token值
    'AUTH_HEADER_TYPES': ('JWT',), # 自定义token头，发请求时token前面要带上
    'USER_ID_FIELD': "uid", # 此处id为生成token时使用自定义的用户表时会使用到，USER_ID_FIELD 是自定义用户表的id，不是id时 会报错user_id = getattr(user, api_settings.USER_ID_FIELD)
    'SIGNING_KEY': SECRET_KEY,  # 签名密钥
    'VERIFYING_KEY': SECRET_KEY,  # 验证密钥
}
ROOT_URLCONF = 'C631Channel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'C631Channel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'c631channel',         # 数据库名，Django不会帮你创建，需要自己进入数据库创建。
        'USER': 'root',       # 设置的数据库用户名
        'PASSWORD': 'root',   # 设置的密码
        'HOST': 'localhost',    # 本地主机或数据库服务器的ip
        'PORT': '3306',         # 数据库使用的端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans' #语言
TIME_ZONE = 'Asia/Shanghai' #时区

USE_I18N = True

USE_TZ = False #不使用UTC时间


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
