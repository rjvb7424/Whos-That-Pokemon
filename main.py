import requests

COUNT = 20
pokemon_names = []

while COUNT != 0:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{COUNT}")
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        pokemon_names.append(name)
    else:
        print("Request failed")
    COUNT -= 1

print(pokemon_names)