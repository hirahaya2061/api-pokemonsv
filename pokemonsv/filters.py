import django_filters as filters

from .models import Pokemons

class PokemonsFilter(filters.FilterSet):
    
    name = filters.CharFilter(method='filter_pokemons_name')
    
    class Meta:
        model = Pokemons
        fields = ['name']
    
    def filter_pokemons_name(self, qs, name, value):
        return qs.filter(name__iexact=value)