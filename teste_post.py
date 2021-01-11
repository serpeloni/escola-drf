import requests

headers = {"Authorization": "Token a1c350c2533d25538c6bd1b95614d9cf8da94c8e"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum",
    "url": "http://geekuniversity.com.br/scrum",
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo do informado
assert resultado.json()["titulo"] == novo_curso["titulo"]