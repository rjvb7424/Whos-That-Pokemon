import requests

COUNT = 5
pokemon_names = []

while COUNT != 0:
    response = requests.get(f"https://pokeapi.co/api/v2/{COUNT}/charmander")
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        pokemon_names[COUNT] = name
    else:
        print("Request failed")
    COUNT -= 1

print(pokemon_names)