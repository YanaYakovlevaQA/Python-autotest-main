import requests
URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "52ac9979326cd22743c069cb8a76bc74"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN }
body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_shange = {
    "pokemon_id": "117625",
    "name": "Pit",
    "photo_id": 1
}

body_catch = {
    "pokemon_id": "117625"
}

'''response = requests.post(url = f"{URL}/trainers/reg", headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f"{URL}/trainers/confirm_email", headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_create)
print(response_create.text)

'''pokemon_id = response_create.json()["id"]
print(pokemon_id)'''

response_change = requests.put(url = f"{URL}/pokemons", headers = HEADER, json = body_shange)
print(response_change.text)

response_catch = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = body_catch)
print(response_catch.text)
