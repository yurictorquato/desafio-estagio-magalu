from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_criar_agendamento():
    payload = {
        "destinatario": "yuri@magalu.com",
        "mensagem": "Completei o desafio!",
        "data_envio": "2026-10-06 10:17:23",
        "canal_comunicacao": "email",
    }

    response = client.post("/agendamentos", json=payload)

    assert response.status_code == 201, response.json()

    dados_resposta = response.json()
    assert "id" in dados_resposta
    assert dados_resposta["status"] == "agendado"
    assert dados_resposta["destinatario"] == "yuri@magalu.com"


def test_consultar_todos_agendamentos():
    payload = [
        {
            "destinatario": "teste_getall@gmail.com",
            "mensagem": "Teste de consulta",
            "data_envio": "2026-10-06T11:44:23",
            "canal_comunicacao": "email"
        },
        {
            "destinatario": "7188258012",
            "mensagem": "Teste de consulta",
            "data_envio": "2026-10-06T11:51:03",
            "canal_comunicacao": "sms"
        }
    ]

    client.post("/agendamentos", json=payload)
    response = client.get("/agendamentos")
    dados_resposta = response.json()

    assert response.status_code == 200
    assert isinstance(dados_resposta, list)
    assert len(dados_resposta) >= 1


def test_consultar_agendamento_pelo_id():
    payload = {
        "destinatario": "teste_get@magalu.com",
        "mensagem": "Teste de consulta",
        "data_envio": "2026-10-06T10:17:23",
        "canal_comunicacao": "email"
    }

    request = client.post("/agendamentos", json=payload)

    id_test = request.json()["id"]
    response = client.get(f"/agendamentos/{id_test}")

    assert response.status_code == 200, response.json()

    dados_resposta = response.json()
    assert dados_resposta["id"] == id_test
    assert dados_resposta["destinatario"] == "teste_get@magalu.com"
