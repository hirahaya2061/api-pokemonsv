from django.contrib.auth.models import User, Group
from .models import *
from .filters import PokemonsFilter
from rest_framework import viewsets
from rest_framework import permissions
import django_filters as filters
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    ユーザ情報の表示・編集を行うAPIのエンドポイント
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    グループ情報の表示・編集を行うAPIのエンドポイント
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = GroupSerializer

class PokemonsViewSet(viewsets.ModelViewSet):
    """
    ポケモン情報の表示・編集を行うAPIのエンドポイント
    """
    queryset = Pokemons.objects.all()
    serializer_class = PokemonsSerializer
    filter_backends = (filters.rest_framework.DjangoFilterBackend,)
    filterset_class = PokemonsFilter

class MovesViewSet(viewsets.ModelViewSet):
    """
    ポケモンのわざの表示・編集を行うAPIのエンドポイント
    """
    queryset = Moves.objects.all()
    serializer_class = MovesSerializer
    