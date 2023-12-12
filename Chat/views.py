from django.http import FileResponse

from .models import UploadedFile
from .serializers import UploadedFileSerializer

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UploadFileView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

class DownloadFileView(RetrieveAPIView):
    queryset = UploadedFile.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.file.path
        response = FileResponse(open(file_path, 'rb'))
        return response

@api_view(['GET'])
def list_uploaded_files(request):
    files = UploadedFile.objects.all()
    serializer = UploadedFileSerializer(files, many=True)
    return Response(serializer.data)

