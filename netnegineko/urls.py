from django.urls import include, path
from rest_framework import routers
from pokemonsv import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'pokemons', views.PokemonsViewSet)
router.register(r'moves', views.MovesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]