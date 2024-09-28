# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model

# from datetime import datetime
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','email','password','profile_image']

    







