import requests


class TestCursos:
    headers = {"Authorization": "Token a1c350c2533d25538c6bd1b95614d9cf8da94c8e"}
    url_base_cursos = "http://localhost:8000/api/v2/cursos/"

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f"{self.url_base_cursos}3/", headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de progrmação em Ruby",
            "url": "http://www.geekuniversity.com.br/cpr",
        }
        resposta = requests.post(
            url=self.url_base_cursos, headers=self.headers, data=novo
        )

        assert resposta.status_code == 201
        assert resposta.json()["titulo"] == novo["titulo"]

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de progrmação em Ruby",
            "url": "http://www.geekuniversity.com.br/ncpr",
        }
        resposta = requests.put(
            url=f"{self.url_base_cursos}3/", headers=self.headers, data=atualizado
        )

        assert resposta.status_code == 200
        assert resposta.json()["titulo"] == atualizado["titulo"]

    def test_delete_curso(self):
        resposta = requests.delete(
            url=f"{self.url_base_cursos}3/", headers=self.headers
        )

        assert resposta.status_code == 204 and len(resposta.text) == 0
