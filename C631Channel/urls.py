from django.urls import re_path,include,path
from django.contrib import admin
# from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # path(r'^admin/', admin.site.urls),
    re_path(r'^user/', include('User.urls')),
    re_path(r'^chat/', include('Chat.urls')),
    # path(r'^docs/', include_docs_urls(title='我的API文档'))
]