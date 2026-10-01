# ANDROID_API

Um projeto mínimo, organizado e didático, com:

- API em FastAPI
- endpoints GET e POST
- interface web em pywebview
- templates Jinja2 com base/header/content
- documentação automática estilo FastAPI
- estrutura de pastas separadas por responsabilidade

## Estrutura

```text
ANDROID_API/
├── app/
│   ├── api/
│   │   └── schemas.py
│   ├── core/
│   │   ├── factory.py
│   │   └── templates.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   └── home.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── pages/
│   │   └── partials/
│   ├── webview/
│   │   ├── __init__.py
│   │   └── launcher.py
│   ├── __init__.py
│   ├── config.py
│   └── tests/
├── main.py
├── requirements.txt
└── README.md
```

## Como rodar

1. Crie o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Rode a API normal:

```bash
python main.py
```

3. Abra a app em webview:

```bash
python main.py --webview
```

A aplicação fica em `http://127.0.0.1:8000` por padrão.

## Como adicionar uma nova rota

A rota é registrada em um arquivo dentro de `app/routes` e exporta uma lista chamada `route_specs`.

Exemplo:

```python
route_specs = [
    {
        "path": "/status",
        "endpoint": get_status,
        "methods": ["GET"],
    }
]
```

Depois, basta importar esse módulo em `app/routes/__init__.py` e ele já entra no app.

## Templates Jinja2

Os templates ficam em `app/templates` e usam um layout compartilhado:

- `base.html`: estrutura principal
- `partials/header.html`: navegação
- `partials/footer.html`: rodapé
- `pages/...`: páginas específicas

Esse desenho deixa cada página simples e reaproveitável.

## Documentação

A documentação da API é gerada automaticamente pelo FastAPI:

- `/docs` → Swagger UI
- `/redoc` → Redoc
- `/openapi.json` → JSON da API

Além disso, existe uma página HTML customizada em `/docs-page` que lê o `openapi()` da aplicação e lista todas as rotas dinamicamente.

## Endpoints de exemplo

- `GET /hello` → retorna uma mensagem de boas-vindas
- `POST /echo` → recebe `{ "message": "texto" }` e devolve o valor recebido

## Fluxo da app webview

O `main.py` inicia o servidor e, quando usado com `--webview`, abre a interface em uma janela desktop com `pywebview`.

Isso mantém a lógica de API separada da lógica de interface visual.
