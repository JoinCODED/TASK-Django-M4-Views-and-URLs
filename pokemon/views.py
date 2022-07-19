from django.http import HttpResponse

from .models import Pokemon
def get_pokemon(request,pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(f"<p>Pokemon name: {pokemon.name}</p>  <p>Pokemon Type: {pokemon.type}</p>  <p>Pokemon power: {pokemon.hp}</p> ")

def get_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemons_list = [f"<li><a href =/pokemons/{pokemon.id} style=color:black;text-decoration:none> {pokemon.name}</li></a>" for pokemon in pokemons]
    return HttpResponse(pokemons_list)