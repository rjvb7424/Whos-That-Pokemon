import requests

COUNT = 20
pokemon_names = []
pokemon_heights = []

while COUNT != 0:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{COUNT}")
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        height = data["height"]
        pokemon_names.append(name)
        pokemon_heights.append(height)
    else:
        print("Request failed")
    COUNT -= 1

COUNT = 19
while COUNT != -1:
    print(f"{pokemon_names[COUNT]} is {pokemon_heights[COUNT]} tall!")
    COUNT -= 1