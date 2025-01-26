import requests

URL = "https://api.pokemonbattle.ru"
token = "Тут должен быть токен"
header = {"Content-type": "application/json", "trainer_token": f"{token}"}
Create_pokemon_body = {"name": "generate", "photo_id": -1}

response = requests.post(
    url=f"{URL}/v2/pokemons", headers=header, json=Create_pokemon_body
)
pokemon_id = response.json()["id"]

print(response.text)

Update_pokemon_body = {
    "pokemon_id": f"{pokemon_id}",
    "name": "generate",
    "photo_id": -1,
}
response = requests.put(
    url=f"{URL}/v2/pokemons", headers=header, json=Update_pokemon_body
)
print(response.text)

catch_pokemon = {"pokemon_id": f"{pokemon_id}"}


response = requests.post(
    url=f"{URL}/v2/trainers/add_pokeball", headers=header, json=catch_pokemon
)
print(response.text)
