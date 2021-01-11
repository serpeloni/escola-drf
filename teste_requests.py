import requests


# GET avaliacoes

# avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

# Acessando o codigo de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# ACessando a quantidade de registros
# print(avaliacoes.json()["count"])

# Acessando a próxima página de resultados
# print(avaliacoes.json()["next"])

# ACessando so resultados desta pagina
# print(avaliacoes.json()["results"])

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()["results"][0])

# Acessando o último elemento da lista de resultados
# print(avaliacoes.json()["results"][-1])

# Acessando somento o nome da pessoa
# print(avaliacoes.json()["results"][-1]["nome"])


# GET  avaliacao
# avaliacao = requests.get("http://localhost:8000/api/v2/avaliacoes/1/")

# print(avaliacao)

# GET cursos
headers = {"Authorization": "Token a1c350c2533d25538c6bd1b95614d9cf8da94c8e"}
cursos = requests.get(url="http://localhost:8000/api/v2/cursos/", headers=headers)

print(cursos.status_code)
print(cursos.json())
