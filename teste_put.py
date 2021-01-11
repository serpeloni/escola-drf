import requests

headers = {"Authorization": "Token a1c350c2533d25538c6bd1b95614d9cf8da94c8e"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://geekuniversity.com.br/ncs3",
}

# buscando curso com ID 5
# curso = requests.get(url=f"{url_base_cursos}5/", headers=headers)

resultado = requests.put(
    url=f"{url_base_cursos}5/", headers=headers, data=curso_atualizado
)

# testando o codigo de status HTTP 200
assert resultado.status_code == 200

# testando o titulo
assert resultado.json()["titulo"] == curso_atualizado["titulo"]
