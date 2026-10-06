# Desafio de Estágio Magalu - API de Agendamento

Este repositório contém a minha solução para o desafio técnico de estágio da LuizaLabs (Magalu). O objetivo do projeto é fornecer uma API RESTful para o agendamento de comunicações (E-mail, SMS, Push, WhatsApp), preparando o terreno para um futuro serviço de envio.

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando um ecossistema moderno em Python:

- **FastAPI:** Framework web principal, escolhido pela sua alta performance e geração automática de documentação (Swagger/OpenAPI).
- **SQLAlchemy 2.0:** ORM (Object Relational Mapper) para modelagem e interação com o banco de dados.
- **Pydantic:** Utilizado para validação estrita de dados de entrada e saída (Schemas).
- **SQLite:** Banco de dados relacional leve utilizado para o ambiente de desenvolvimento local.
- **Pytest & TestClient:** Ferramentas para a criação e execução de testes automatizados.
- **Uvicorn:** Servidor ASGI para rodar a aplicação.

## ⚙️ Arquitetura

A aplicação segue o padrão de **Arquitetura em Camadas** para manter as responsabilidades separadas e o código limpo:

- `models/`: Entidades de banco de dados (SQLAlchemy).
- `schemas/`: Regras de validação e tipagem de I/O (Pydantic).
- `routers/`: Controladores responsáveis por receber as requisições HTTP e devolver as respostas.
- `configs/`: Configurações de conexão com o banco de dados.

## 📌 Endpoints da API

A API possui três rotas principais focadas na gestão do agendamento:

| Método | Rota                  | Descrição                                                                                                                                                                    |
| ------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `POST` | `/agendamentos`       | Cria um novo agendamento. Recebe o destinatário, a mensagem, a data e hora do envio e o canal de comunicação. O status inicial é salvo automaticamente como `AGENDADO`.      |
| `GET`  | `/agendamentos`       | Retorna uma lista com todos os agendamentos cadastrados no banco de dados.                                                                                                   |
| `GET`  | `/agendamentos/{id}`  | Consulta o status e as informações de um agendamento específico através do seu UUID.                                                                                         |

## 💻 Como Executar o Projeto

### Pré-requisitos

- Python 3.13+ instalado.
- Gerenciador de pacotes (`uv`).

### Passo a Passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/yurictorquato/desafio-estagio-magalu.git
   cd desafio-estagio-magalu
   ```

2. Instale as dependências (exemplo usando o `uv`, que foi utilizado no projeto):

   ```bash
   uv sync
   ```

3. Navegue até a pasta do código-fonte e inicie o servidor local:

   ```bash
   cd src
   uvicorn main:app --reload
   ```

4. Acesse a documentação interativa (Swagger) no seu navegador:

   👉 http://127.0.0.1:8000/docs

## 🧪 Como Rodar os Testes

O projeto possui cobertura de testes unitários para garantir o funcionamento correto de todas as rotas de forma independente.

Para executar a suíte de testes, basta rodar o comando abaixo na raiz do projeto:

```bash
pytest
```