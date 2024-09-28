# from django.contrib.auth.models import User
from .models import CustomUser
from django.conf import settings
from rest_framework import viewsets
from rest_framework import permissions
from app.serializer import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
	
