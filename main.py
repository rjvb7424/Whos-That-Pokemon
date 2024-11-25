import random
import requests

def fetch_pokemon_name(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    return response.json()["name"]

def fetch_pokemon_database(database_size: int):
    pokemon_database = []
    while database_size > 0:
        pokemon_name = fetch_pokemon_name(database_size)
        pokemon_database.append(pokemon_name)
        database_size -= 1
    return pokemon_database

pokemon_database = fetch_pokemon_database(50)

def pick_pokemon(pokemon_database):
    return random.choice(pokemon_database)

picked_pokemon = pick_pokemon(pokemon_database)

def name_for_underscores(picked_pokemon):
    return ["_" for _ in picked_pokemon]

hidden_pokemon = name_for_underscores(picked_pokemon)

def hint_system(hidden_pokemon, picked_pokemon):
    while True:
        reveal_character = random.randint(0, len(hidden_pokemon) - 1)
        if hidden_pokemon[reveal_character] == "_":
            hidden_pokemon[reveal_character] = picked_pokemon[reveal_character]
            break
    return hidden_pokemon

user_input = ""
while user_input != picked_pokemon:
    if ''.join(hidden_pokemon) == picked_pokemon:
        break
    print(f"\033[33m{''.join(hidden_pokemon)}\033[0m")
    user_input = input("\033[31mWho's that Pokemon?!\033[0m ")
    print()
    hidden_pokemon = hint_system(hidden_pokemon, picked_pokemon)

print(f"\033[33mIt's {picked_pokemon}!\033[0m")