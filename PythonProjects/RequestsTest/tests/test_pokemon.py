import requests
import pytest

URL = "https://api.pokemonbattle.ru"
token = "Тут должен быть токен"
header = {"Content-type": "application/json", "trainer_token": f"{token}"}
Create_pokemon_body = {"name": "generate", "photo_id": -1}


def test_get_trainers_200():
    response = requests.get(url=f"{URL}/v2/trainers")
    assert response.status_code == 200


def test_my_trainer_id():
    response = requests.get(url=f"{URL}/v2/trainers", params={"trainer_id": 17962})
    assert response.json()["data"][0]["id"] == "17962"
