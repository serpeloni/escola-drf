import requests

headers = {"Authorization": "Token a1c350c2533d25538c6bd1b95614d9cf8da94c8e"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()["count"] == 1

# Testando se o titulo do primeiro curso está correto
assert resultado.json()["results"][0]["titulo"] == "Programação com Javascript"
