from django.urls import path
from .views import UploadFileView, DownloadFileView, list_uploaded_files

urlpatterns = [
    path('uploadfile', UploadFileView.as_view(), name='upload_file'),
    path('downloadById/<int:pk>', DownloadFileView.as_view(), name='download_file'),
    path('getAllfile', list_uploaded_files, name='list_uploaded_files'),
]
