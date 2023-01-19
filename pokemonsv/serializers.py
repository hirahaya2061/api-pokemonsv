from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class PokemonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemons
        fields = ['dex_no',
                  'name',
                  'form',
                  'type1',
                  'type2',
                  'ability1',
                  'ability2',
                  'ability_d',
                  'hp',
                  'attack',
                  'defence',
                  'sp_attack',
                  'sp_defence',
                  'speed']


class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = ['name',
                  'class_field',
                  'type',
                  'pp',
                  'power',
                  'accury',
                  'area',
                  'priority',
                  'direct',
                  'number_times_max',
                  'number_times_min',
                  'direct',
                  'on_hit',
                  'machine_no']
        

