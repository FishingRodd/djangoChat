from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['uid','username','nickname','password']
        fields = '__all__'
        # exclude = ('password',)
        read_only_fields = ['uid']