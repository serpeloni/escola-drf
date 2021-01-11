import requests

headers = {"Authorization": "Token a1c350c2533d25538c6bd1b95614d9cf8da94c8e"}

url_base_cursos = "http://localhost:8000/api/v2/cursos/"
url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

resultado = requests.delete(url=f"{url_base_cursos}5/", headers=headers)

# testando codigo de status HTTP 204
assert resultado.status_code == 204

# testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0