from rest_framework import generics
import django_filters.rest_framework as filters
from .serializers import UserSerializer
from .models import User



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['date_of_registration',]

